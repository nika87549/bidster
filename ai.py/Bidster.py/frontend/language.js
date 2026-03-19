async function loadLanguage(lang) {
    const response = await fetch(`./i18n/${lang}.json`);
    const translations = await response.json();

    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        el.textContent = translations[key];
    });
}

// ენის შეცვლა
function changeLanguage(lang) {
    localStorage.setItem("lang", lang);
    loadLanguage(lang);
}

// პირველ ჩატვირთვაზე
document.addEventListener("DOMContentLoaded", () => {
    const savedLang = localStorage.getItem("lang") || "en";
    loadLanguage(savedLang);
});