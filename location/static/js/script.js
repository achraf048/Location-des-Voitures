// 🎬 Fade-in animation on scroll with Intersection Observer
const cards = document.querySelectorAll(".card");

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

cards.forEach(card => {
    observer.observe(card);
});

// 🔍 Search + Filter functionality
const searchInput = document.getElementById("searchInput");
const categoryFilter = document.getElementById("categoryFilter");
const fuelFilter = document.getElementById("fuelFilter");
const resetFiltersBtn = document.getElementById("resetFiltersBtn");
const resetEmptyBtn = document.getElementById("resetEmptyBtn");
const carGrid = document.getElementById("carGrid");
const emptyState = document.getElementById("emptyState");

function filterCars() {
    const searchValue = searchInput ? searchInput.value.toLowerCase().trim() : "";
    const categoryValue = categoryFilter ? categoryFilter.value : "";
    const fuelValue = fuelFilter ? fuelFilter.value : "";
    
    let visibleCount = 0;
    const cards = document.querySelectorAll(".card");
    
    cards.forEach(card => {
        const name = card.dataset.name ? card.dataset.name.toLowerCase() : "";
        const category = card.dataset.category || "";
        const fuel = card.dataset.fuel || "";
        
        const matchesSearch = name.includes(searchValue);
        const matchesCategory = (categoryValue === "" || category === categoryValue);
        const matchesFuel = (fuelValue === "" || fuel === fuelValue);
        
        if (matchesSearch && matchesCategory && matchesFuel) {
            card.style.display = "block";
            visibleCount++;
        } else {
            card.style.display = "none";
        }
    });
    
    // Show/hide empty state
    if (cards.length > 0 && visibleCount === 0) {
        if (emptyState) emptyState.style.display = "block";
        if (carGrid) carGrid.style.display = "none";
    } else {
        if (emptyState) emptyState.style.display = "none";
        if (carGrid) carGrid.style.display = "grid";
    }
}

// Event listeners for search and filter
if (searchInput) searchInput.addEventListener("keyup", filterCars);
if (categoryFilter) categoryFilter.addEventListener("change", filterCars);
if (fuelFilter) fuelFilter.addEventListener("change", filterCars);

// Reset filters
function resetFilters() {
    if (searchInput) searchInput.value = "";
    if (categoryFilter) categoryFilter.value = "";
    if (fuelFilter) fuelFilter.value = "";
    filterCars();
}

if (resetFiltersBtn) resetFiltersBtn.addEventListener("click", resetFilters);
if (resetEmptyBtn) resetEmptyBtn.addEventListener("click", resetFilters);

// 🎯 Header shadow on scroll
window.addEventListener("scroll", () => {
    const header = document.getElementById("header");
    if (window.scrollY > 10) {
        header.style.boxShadow = "0 2px 20px rgba(0, 0, 0, 0.08)";
    } else {
        header.style.boxShadow = "none";
    }
});

// 🚀 Rent button animation
document.querySelectorAll(".order-btn").forEach(btn => {
    btn.addEventListener("click", (e) => {
        e.preventDefault();
        const carName = btn.getAttribute("data-car") || "Selected vehicle";
        const originalText = btn.innerHTML;
        
        btn.innerHTML = '<i class="fas fa-check"></i> Rented!';
        btn.style.background = "#28a745";
        btn.disabled = true;
        
        showNotification(`${carName} added to your rentals. Check your email for confirmation.`);
        
        setTimeout(() => {
            btn.innerHTML = originalText;
            btn.style.background = "var(--primary)";
            btn.disabled = false;
        }, 3000);
    });
});

// Toast notification
function showNotification(message) {
    let toast = document.querySelector(".custom-toast");
    if (!toast) {
        toast = document.createElement("div");
        toast.className = "custom-toast";
        toast.style.cssText = `
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: var(--gray-900);
            color: white;
            padding: 14px 24px;
            border-radius: 12px;
            font-weight: 500;
            z-index: 10000;
            box-shadow: var(--shadow-lg);
            transform: translateX(450px);
            transition: transform 0.3s ease;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 10px;
        `;
        document.body.appendChild(toast);
    }
    
    toast.innerHTML = `<i class="fas fa-check-circle" style="color: #28a745;"></i> ${message}`;
    toast.style.transform = "translateX(0)";
    
    setTimeout(() => {
        toast.style.transform = "translateX(450px)";
    }, 4000);
}

// Mobile menu toggle (optional enhancement)
const mobileBtn = document.getElementById("mobileMenuBtn");
if (mobileBtn) {
    mobileBtn.addEventListener("click", () => {
        const nav = document.querySelector("nav");
        const actions = document.querySelector(".header-actions");
        if (nav && actions) {
            nav.style.display = nav.style.display === "flex" ? "none" : "flex";
            actions.style.display = actions.style.display === "flex" ? "none" : "flex";
            if (nav.style.display === "flex") {
                nav.style.flexDirection = "column";
                nav.style.position = "absolute";
                nav.style.top = "70px";
                nav.style.left = "0";
                nav.style.right = "0";
                nav.style.background = "white";
                nav.style.padding = "20px";
                nav.style.boxShadow = "var(--shadow-md)";
                actions.style.position = "absolute";
                actions.style.top = "70px";
                actions.style.right = "20px";
                actions.style.background = "white";
                actions.style.padding = "10px";
                actions.style.borderRadius = "12px";
                actions.style.boxShadow = "var(--shadow-md)";
            } else {
                nav.style.position = "";
                actions.style.position = "";
            }
        }
    });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== "#" && href !== "#header" && href !== "#") {
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    });
});

// Initialize filter on load
setTimeout(() => {
    filterCars();
}, 100);