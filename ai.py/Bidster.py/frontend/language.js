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




// ენების ბაზა
const translations = {
    'en': {
        'welcome': 'Welcome to Bidster',
        'active_auctions': 'Active Auctions',
        'finished_auctions': 'Finished Auctions',
        'login': 'Login',
        'register': 'Register'
    },
    'ka': {
        'welcome': 'მოგესალმებით Bidster-ზე',
        'active_auctions': 'აქტიური აუქციონები',
        'finished_auctions': 'დასრულებული აუქციონები',
        'login': 'შესვლა',
        'register': 'რეგისტრაცია'
    }
    // აქ შეგიძლია სხვა ენებიც დაამატო (de, fr და ა.შ.)
};

function changeLanguage(lang) {
    // ვპოულობთ ყველა ელემენტს, რომელსაც აქვს data-i18n ატრიბუტი
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        // თუ თარგმანი არსებობს, ვცვლით ტექსტს
        if (translations[lang] && translations[lang][key]) {
            element.textContent = translations[lang][key];
        }
    });
    
    // ვიმახსოვრებთ არჩეულ ენას, რომ გვერდის გადატვირთვისას არ დაიკარგოს
    localStorage.setItem('selectedLanguage', lang);
}

// როცა გვერდი ჩაიტვირთება, ბოლოს არჩეული ენა დააყენოს
window.onload = () => {
    const savedLang = localStorage.getItem('selectedLanguage') || 'ka';
    changeLanguage(savedLang);
};