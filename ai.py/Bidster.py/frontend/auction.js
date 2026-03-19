const AUCTION_ID = 1;   // დროებით fix
const USER_ID = 1;      // დროებით fix

async function fetchStatus() {
    const res = await fetch(`http://127.0.0.1:5000/api/auction/status/${AUCTION_ID}`);
    const data = await res.json();
    if (data.error) return;

    // ტაიმერი
    const sec = data.remaining_seconds;
    const h = String(Math.floor(sec / 3600)).padStart(2, "0");
    const m = String(Math.floor((sec % 3600) / 60)).padStart(2, "0");
    const s = String(sec % 60).padStart(2, "0");
    document.getElementById("timer").textContent = `${h}:${m}:${s}`;

    // ბოლო ბიდერი / თანხა
    document.getElementById("last-bidder").textContent = data.last_bidder_id ?? "-";
    document.getElementById("last-amount").textContent = data.last_bid_amount ?? "-";
}

async function placeBid() {
    const res = await fetch("http://127.0.0.1:5000/api/auction/bid", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({auction_id: AUCTION_ID, user_id: USER_ID})
    });
    const data = await res.json();
    console.log(data);
    fetchStatus();
}

document.addEventListener("DOMContentLoaded", () => {
    fetchStatus();
    setInterval(fetchStatus, 1000); // „live“ განახლება ყოველ წამში
});



async function loadChat() {
    const res = await fetch(`http://127.0.0.1:5000/api/chat/get/${AUCTION_ID}`);
    const messages = await res.json();

    const box = document.getElementById("chat-box");
    box.innerHTML = "";

    messages.forEach(m => {
        const div = document.createElement("div");
        div.textContent = `User ${m.user_id}: ${m.text}`;
        box.appendChild(div);
    });

    box.scrollTop = box.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById("chat-input");
    const text = input.value.trim();
    if (!text) return;

    await fetch("http://127.0.0.1:5000/api/chat/send", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            user_id: USER_ID,
            auction_id: AUCTION_ID,
            text: text
        })
    });

    input.value = "";
    loadChat();
}

setInterval(loadChat, 1000); // live update



const socket = io("http://127.0.0.1:5000");

// შევდივართ აუქციონის ოთახში
socket.emit("join_room", { auction_id: AUCTION_ID });

// მესიჯის მიღება რეალურ დროში
socket.on("new_message", (data) => {
    const box = document.getElementById("chat-box");
    const div = document.createElement("div");
    div.textContent = `User ${data.user_id}: ${data.text}`;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
});

// მესიჯის გაგზავნა
function sendMessage() {
    const input = document.getElementById("chat-input");
    const text = input.value.trim();
    if (!text) return;

    socket.emit("send_message", {
        user_id: USER_ID,
        auction_id: AUCTION_ID,
        text: text
    });

    input.value = "";
}





async function loadAuctionInfo() {
    const res = await fetch(`http://127.0.0.1:5000/api/auction/get/${AUCTION_ID}`);
    const data = await res.json();

    document.getElementById("auction-image").src = data.image_url;
    document.getElementById("auction-title-text").textContent = data.title;
    document.getElementById("auction-description").textContent = data.description;

    document.getElementById("start-price").textContent = data.start_price + " ₾";
    document.getElementById("ticket-price").textContent = data.ticket_price + " ₾";
    document.getElementById("total-tickets").textContent = data.total_tickets_available;
    document.getElementById("tickets-sold").textContent = data.total_tickets_sold;
}




document.addEventListener("DOMContentLoaded", () => {
    loadAuctionInfo();
    loadChat();
    startTimer();
});