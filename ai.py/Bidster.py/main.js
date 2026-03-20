async function buyTicketStripe(auctionId, userId) {
    const res = await fetch("http://127.0.0.1:5000/api/payments/stripe/create_payment", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({auction_id: auctionId, user_id: userId})
    });
    const data = await res.json();
    if (data.checkout_url) {
        window.location.href = data.checkout_url;
    }
}

async function buyTicketPayPal(auctionId, userId) {
    const res = await fetch("http://127.0.0.1:5000/api/payments/paypal/create_payment", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({auction_id: auctionId, user_id: userId})
    });
    const data = await res.json();
    if (data.approve_url) {
        window.location.href = data.approve_url;
    }
}