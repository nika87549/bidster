const USER_ID = 1; // დროებით

async function loadProfile() {
    const res = await fetch(`http://127.0.0.1:5000/api/auth/profile/${USER_ID}`);
    const data = await res.json();
    if (data.error) return;

    document.getElementById("email").textContent = "Email: " + data.email;
    document.getElementById("country").textContent = "Country: " + data.country;
    if (data.avatar_url) {
        document.getElementById("avatar").src = "http://127.0.0.1:5000" + data.avatar_url;
    } else {
        document.getElementById("avatar").src = "https://via.placeholder.com/120";
    }
}

document.getElementById("avatar-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById("avatar-input");
    if (!fileInput.files[0]) return;

    const formData = new FormData();
    formData.append("avatar", fileInput.files[0]);

    const res = await fetch(`http://127.0.0.1:5000/api/profile/upload_avatar/${USER_ID}`, {
        method: "POST",
        body: formData
    });
    const data = await res.json();
    console.log(data);
    loadProfile();
});

document.addEventListener("DOMContentLoaded", loadProfile);