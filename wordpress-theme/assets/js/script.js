// ================================================
// THE WALL STREET COACH - MAIN JAVASCRIPT
// ================================================

// Mobile Navigation Toggle
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const navLinks = document.getElementById('navLinks');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        mobileMenuToggle.classList.toggle('active');
    });

    // Close menu when clicking a link
    const links = navLinks.querySelectorAll('.nav-link');
    links.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            mobileMenuToggle.classList.remove('active');
        });
    });
}

// ================================================
// Sticky Navigation on Scroll
// ================================================

const mainNav = document.getElementById('mainNav');
let lastScrollTop = 0;

window.addEventListener('scroll', () => {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop && scrollTop > 100) {
        // Scrolling down
        mainNav.style.transform = 'translateY(-100%)';
    } else {
        // Scrolling up
        mainNav.style.transform = 'translateY(0)';
    }

    lastScrollTop = scrollTop;
});

// ================================================
// Scroll Progress Indicator
// ================================================

const scrollProgress = document.getElementById('scrollProgress');

if (scrollProgress) {
    const updateProgress = () => {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        scrollProgress.style.width = `${progress}%`;
    };

    window.addEventListener('scroll', updateProgress);
    window.addEventListener('resize', updateProgress);
    updateProgress();
}

// ================================================
// Sticky Mobile CTA - Show on Scroll
// ================================================

const stickyCTA = document.getElementById('stickyCTA');

if (stickyCTA) {
    window.addEventListener('scroll', () => {
        if (window.innerWidth <= 768) {
            if (window.pageYOffset > 500) {
                stickyCTA.style.display = 'block';
            } else {
                stickyCTA.style.display = 'none';
            }
        } else {
            stickyCTA.style.display = 'none';
        }
    });
}

// ================================================
// Smooth Scroll for Anchor Links
// ================================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');

        // Only handle internal anchors, not empty hashes
        if (href !== '#' && href !== '') {
            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// ================================================
// Form Handling
// ================================================

// Contact Form
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        // Get form data
        const formData = new FormData(contactForm);
        const data = Object.fromEntries(formData);

        // Here you would normally send the data to your backend
        console.log('Contact form submitted:', data);

        // Show success message
        alert('Thank you for your inquiry! We will be in touch soon.');
        contactForm.reset();
    });
}

// Lead Magnet Forms
const leadForms = document.querySelectorAll('.lead-form');
leadForms.forEach(form => {
    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const email = form.querySelector('input[type="email"]').value;

        // Here you would normally send the email to your backend/email service
        console.log('Lead magnet requested:', email);

        // Show success message
        alert('Success! Check your email for your free resource.');
        form.reset();
    });
});

// Newsletter Form
const newsletterForm = document.querySelector('.newsletter-form');
if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const email = newsletterForm.querySelector('input[type="email"]').value;

        // Here you would normally send the email to your backend/email service
        console.log('Newsletter subscription:', email);

        // Show success message
        alert('Welcome to the Inner Circle! Check your email for confirmation.');
        newsletterForm.reset();
    });
}

// ================================================
// FAQ Accordion (if needed in future)
// ================================================

const faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach(item => {
    const question = item.querySelector('h3');
    if (question) {
        question.style.cursor = 'pointer';
        question.addEventListener('click', () => {
            item.classList.toggle('active');
        });
    }
});

// ================================================
// Lazy Loading for Images (when images are added)
// ================================================

if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            }
        });
    });

    const images = document.querySelectorAll('img[data-src]');
    images.forEach(img => imageObserver.observe(img));
}

// ================================================
// Fade-in Animation on Scroll
// ================================================

const observeElements = document.querySelectorAll('.feature-card, .path-card, .testimonial-card, .step-card');

const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '0';
            entry.target.style.transform = 'translateY(20px)';

            setTimeout(() => {
                entry.target.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }, 100);

            fadeObserver.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.1
});

observeElements.forEach(el => fadeObserver.observe(el));

// ================================================
// Animated Counters (hero stats, etc.)
// ================================================

const counterElements = document.querySelectorAll('[data-counter]');

if (counterElements.length) {
    const animateCounter = (element) => {
        const target = parseFloat(element.dataset.target || '0');
        const duration = parseInt(element.dataset.duration || '1500', 10);
        const suffix = element.dataset.suffix || '';
        const prefix = element.dataset.prefix || '';
        const decimals = parseInt(element.dataset.decimals || '0', 10);

        const startTime = performance.now();

        const step = (now) => {
            const progress = Math.min((now - startTime) / duration, 1);
            const value = target * progress;
            const displayValue = decimals > 0 ? value.toFixed(decimals) : Math.round(value);
            element.textContent = `${prefix}${displayValue}${suffix}`;

            if (progress < 1) {
                requestAnimationFrame(step);
            }
        };

        requestAnimationFrame(step);
    };

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counterElements.forEach(counter => {
        counter.textContent = `${counter.dataset.prefix || ''}0${counter.dataset.suffix || ''}`;
        counterObserver.observe(counter);
    });
}

// ================================================
// Initialize on DOM Load
// ================================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('The Wall Street Coach website initialized');

    // FIX: Podcast Page Navigation Menu Regression (Fallback - Aggressive)
    if (window.location.href.includes('/episodes/') || document.body.classList.contains('single-podcast')) {
        const navLinks = document.querySelectorAll('.nav-link, .menu-item a');
        navLinks.forEach(link => {
            const text = link.textContent.trim().toLowerCase();
            if (text.includes('resource')) {
                console.log('Applying Nav Fix: Resources -> Tools');
                link.textContent = 'Tools';
                link.href = '/tools';
            }
        });
    }

    // Add any initialization code here
});

// ================================================
// TPI Diamond Animation (if needed)
// ================================================

const tpiDiamond = document.querySelector('.tpi-diamond');
if (tpiDiamond) {
    const polygon = tpiDiamond.querySelector('polygon');

    if (polygon) {
        // Animate the polygon on page load
        polygon.style.opacity = '0';

        setTimeout(() => {
            polygon.style.transition = 'opacity 1s ease';
            polygon.style.opacity = '1';
        }, 500);
    }
}

// ================================================
// Testimonial Carousel
// ================================================

const testimonialSlides = document.querySelectorAll('.testimonial-slide');
if (testimonialSlides.length > 0) {
    let currentSlide = 0;
    const slideInterval = 5000; // 5 seconds

    const nextSlide = () => {
        testimonialSlides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % testimonialSlides.length;
        testimonialSlides[currentSlide].classList.add('active');
    };

    setInterval(nextSlide, slideInterval);
}

// ================================================
// Pricing Card Hover Effects Enhancement
// ================================================

const pricingCards = document.querySelectorAll('.pricing-card');
pricingCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        pricingCards.forEach(c => {
            if (c !== card) {
                c.style.opacity = '0.7';
            }
        });
    });

    card.addEventListener('mouseleave', () => {
        pricingCards.forEach(c => {
            c.style.opacity = '1';
        });
    });
});

// ================================================
// Custom Cursor Effect (Optional Enhancement)
// ================================================

const addCustomCursor = () => {
    const buttons = document.querySelectorAll('.btn-primary, .btn-secondary, .btn-cta');

    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.cursor = 'pointer';
        });
    });
};

addCustomCursor();

// ================================================
// Page Transition Effect
// ================================================

// Fade in page on load
document.body.style.opacity = '0';
window.addEventListener('load', () => {
    document.body.style.transition = 'opacity 0.5s ease';
    document.body.style.opacity = '1';
});

// ================================================
// Analytics Integration (Template)
// ================================================

// Function to track button clicks
const trackButtonClick = (buttonName) => {
    console.log(`Button clicked: ${buttonName}`);

    // Example: Google Analytics tracking
    // if (typeof gtag !== 'undefined') {
    //     gtag('event', 'button_click', {
    //         'button_name': buttonName
    //     });
    // }
};

// Add tracking to all CTA buttons
const ctaButtons = document.querySelectorAll('.btn-cta, .btn-primary');
ctaButtons.forEach(button => {
    button.addEventListener('click', () => {
        const buttonText = button.textContent.trim();
        trackButtonClick(buttonText);
    });
});

// ================================================
// Free Ebook Bundle Bottom Bar Popup
// ================================================

const createEbookPopup = () => {
    // Check if user already dismissed
    if (localStorage.getItem('ebookPopupDismissed_v2')) {
        return;
    }

    // Create the popup HTML with 3-column layout
    const popupHTML = `
        <div id="ebookPopup" class="ebook-popup">
            <div class="ebook-popup-glow"></div>
            <div class="ebook-popup-content">
                <div class="ebook-popup-col ebook-popup-col-left">
                    <div class="ebook-popup-badge">FREE RESOURCES</div>
                </div>
                <div class="ebook-popup-col ebook-popup-col-center">
                    <h4 class="ebook-popup-title">Get "The 5 Practices" Free</h4>
                    <p class="ebook-popup-subtitle">Simple strategies to master discipline & overcome fear.</p>
                </div>
                <div class="ebook-popup-col ebook-popup-col-right">
                    <a href="/download" class="ebook-popup-btn">Claim Free Copy</a>
                </div>
                <button class="ebook-popup-close" aria-label="Close popup">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </button>
            </div>
        </div>
    `;

    // Add CSS styles - 3 column balanced layout
    const popupStyles = `
        <style>
            .ebook-popup {
                position: fixed;
                bottom: -150px;
                left: 0;
                right: 0;
                background: #08333A;
                color: #fff;
                z-index: 9999;
                box-shadow: 0 -8px 32px rgba(0,0,0,0.25);
                transition: bottom 0.5s cubic-bezier(0.4, 0, 0.2, 1);
                padding: 1rem 2rem;
                border-top: 1px solid rgba(201, 162, 39, 0.3);
                overflow: hidden;
            }
            .ebook-popup-glow {
                position: absolute;
                top: 0;
                left: 50%;
                transform: translateX(-50%);
                width: 400px;
                height: 2px;
                background: linear-gradient(90deg, transparent, #C9A227, transparent);
            }
            .ebook-popup.show {
                bottom: 0;
            }
            .ebook-popup-content {
                max-width: 1200px;
                margin: 0 auto;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 2rem;
            }
            .ebook-popup-col {
                display: flex;
                align-items: center;
            }
            .ebook-popup-col-left {
                flex: 0 0 auto;
            }
            .ebook-popup-col-center {
                flex: 1;
                text-align: center;
                flex-direction: column;
            }
            .ebook-popup-col-right {
                flex: 0 0 auto;
                gap: 1rem;
            }
            .ebook-popup-badge {
                display: inline-block;
                background: rgba(201, 162, 39, 0.15);
                color: #C9A227;
                font-size: 0.7rem;
                font-weight: 700;
                letter-spacing: 1.5px;
                padding: 0.5rem 1rem;
                border-radius: 4px;
                border: 1px solid rgba(201, 162, 39, 0.3);
                white-space: nowrap;
            }
            .ebook-popup-title {
                font-size: 1.1rem;
                font-weight: 600;
                margin: 0 0 0.25rem 0;
                color: #fff;
                font-family: 'Playfair Display', serif;
            }
            .ebook-popup-subtitle {
                font-size: 0.85rem;
                color: rgba(255,255,255,0.6);
                margin: 0;
                font-weight: 400;
            }
            .ebook-popup-actions {
                display: flex;
                align-items: center;
                gap: 1.5rem;
                flex-shrink: 0;
            }
            .ebook-popup-btn {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                background: linear-gradient(135deg, #C9A227 0%, #d4af37 100%);
                color: #08333A;
                padding: 0.75rem 1.75rem;
                border-radius: 6px;
                text-decoration: none;
                font-weight: 700;
                font-size: 0.9rem;
                transition: all 0.3s;
                white-space: nowrap;
                box-shadow: 0 4px 15px rgba(201, 162, 39, 0.3);
            }
            .ebook-popup-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(201, 162, 39, 0.4);
            }
            .ebook-popup-close {
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 8px;
                color: rgba(255,255,255,0.6);
                cursor: pointer;
                padding: 0.65rem;
                transition: all 0.3s;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 42px;
                height: 42px;
                margin-left: 1.5rem;
                flex-shrink: 0;
            }
            .ebook-popup-close:hover {
                background: rgba(255,255,255,0.1);
                color: #fff;
                border-color: rgba(255,255,255,0.2);
            }
            @media (max-width: 768px) {
                .ebook-popup {
                    display: none !important;
                }
            }
        </style>
    `;

    // Insert styles and popup
    document.head.insertAdjacentHTML('beforeend', popupStyles);
    document.body.insertAdjacentHTML('beforeend', popupHTML);

    const popup = document.getElementById('ebookPopup');
    const closeBtn = popup.querySelector('.ebook-popup-close');

    // Show popup after 5 seconds or 30% scroll
    let popupShown = false;

    const showPopup = () => {
        if (!popupShown) {
            popup.classList.add('show');
            popupShown = true;
        }
    };

    // Timer trigger
    setTimeout(showPopup, 5000);

    // Scroll trigger
    window.addEventListener('scroll', () => {
        const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
        if (scrollPercent > 30) {
            showPopup();
        }
    });

    // Exit Intent Trigger (Full Screen Popup)
    document.addEventListener('mouseleave', (e) => {
        if (e.clientY < 50) {
            createExitPopup();
        }
    });

    // Close button
    closeBtn.addEventListener('click', () => {
        popup.classList.remove('show');
        localStorage.setItem('ebookPopupDismissed_v2', 'true');
    });

    // Also close when clicking the CTA (they're going to resources)
    const ctaBtn = popup.querySelector('.ebook-popup-btn');
    if (ctaBtn) {
        ctaBtn.addEventListener('click', () => {
            localStorage.setItem('ebookPopupDismissed_v2', 'true');
        });
    }
};

// ================================================
// Full Screen Exit Intent Popup (The 5 Practices)
// ================================================

const createExitPopup = () => {
    // Check if user already dismissed
    if (localStorage.getItem('exitIntentDismissed')) {
        return;
    }

    // Create the popup HTML
    const popupHTML = `
        <div id="exitIntentPopup" class="exit-popup-overlay">
            <div class="exit-popup-container">
                <button class="exit-popup-close" aria-label="Close popup">&times;</button>
                <div class="exit-popup-grid">
                    <!-- Left Column: Copy & Book -->
                    <div class="exit-popup-content">
                        <h2 style="color: var(--navy); margin-bottom: 1rem; font-size: 2rem; line-height: 1.2;">Stop Sabotaging Your Trades. Start Mastering Your Mind.</h2>
                        <p style="color: var(--gold); font-family: 'Space Mono', monospace; text-transform: uppercase; font-weight: 700; letter-spacing: 1px; font-size: 0.8rem; margin-bottom: 1.5rem;">
                            The 5 Proven Practices Used by Top 1% Traders
                        </p>
                        
                        <div style="margin-bottom: 1.5rem; text-align: center;">
                            <img src="/wp-content/themes/twsc-theme/assets/images/5-practices-tools.jpg" alt="The 5 Practices" style="width: 100%; height: auto; box-shadow: 0 10px 20px rgba(0,0,0,0.15); border-radius: 4px;">
                        </div>
                    </div>

                    <!-- Right Column: Form -->
                    <div class="exit-popup-form">
                        <div style="width:100%; height:100%; min-height: 500px;">
                            <iframe
                                src="https://link.fgfunnels.com/widget/form/P4QzMatpx421RnihwZsq"
                                style="width:100%;height:100%;border:none;border-radius:4px"
                                id="popup-inline-P4QzMatpx421RnihwZsq" 
                                data-layout="{'id':'INLINE'}"
                                data-trigger-type="alwaysShow"
                                data-trigger-value=""
                                data-activation-type="alwaysActivated"
                                data-activation-value=""
                                data-deactivation-type="neverDeactivate"
                                data-deactivation-value=""
                                data-form-name="5 Practices - Sign Up (2026)"
                                data-height="550"
                                data-layout-iframe-id="popup-inline-P4QzMatpx421RnihwZsq"
                                data-form-id="P4QzMatpx421RnihwZsq"
                                title="5 Practices - Sign Up (2026)"
                            ></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;

    // Add CSS styles
    const popupStyles = `
        <style>
            .exit-popup-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(8, 51, 58, 0.85);
                backdrop-filter: blur(5px);
                z-index: 10000;
                display: flex;
                align-items: center;
                justify-content: center;
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease;
                padding: 1rem;
            }
            .exit-popup-overlay.show {
                opacity: 1;
                visibility: visible;
            }
            .exit-popup-container {
                background: #fff;
                width: 100%;
                max-width: 900px;
                border-radius: 12px;
                position: relative;
                transform: scale(0.95);
                transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
                overflow: hidden;
                max-height: 90vh;
                overflow-y: auto;
            }
            .exit-popup-overlay.show .exit-popup-container {
                transform: scale(1);
            }
            .exit-popup-close {
                position: absolute;
                top: 1rem;
                right: 1rem;
                background: transparent;
                border: none;
                font-size: 2rem;
                line-height: 1;
                color: var(--navy);
                cursor: pointer;
                z-index: 10;
                padding: 0.5rem;
                transition: color 0.2s;
            }
            .exit-popup-close:hover {
                color: var(--gold);
            }
            .exit-popup-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
            }
            .exit-popup-content {
                padding: 3rem;
                background: #F9F9F7;
                border-right: 1px solid rgba(0,0,0,0.05);
            }
            .exit-popup-form {
                padding: 2rem;
                background: #fff;
            }
            
            @media (max-width: 768px) {
                .exit-popup-grid {
                    grid-template-columns: 1fr;
                }
                .exit-popup-content {
                    padding: 2rem;
                    text-align: center;
                }
                .exit-popup-content img {
                    display: none; /* Hide image on mobile to save space */
                }
                .exit-popup-form {
                    padding: 1rem;
                }
            }
        </style>
    `;

    // Insert styles and popup
    if (!document.getElementById('exitIntentPopupStyles')) {
        document.head.insertAdjacentHTML('beforeend', `<div id="exitIntentPopupStyles">${popupStyles}</div>`);
    }
    if (!document.getElementById('exitIntentPopup')) {
        document.body.insertAdjacentHTML('beforeend', popupHTML);
    }

    const popup = document.getElementById('exitIntentPopup');
    const closeBtn = popup.querySelector('.exit-popup-close');

    // Show popup
    // Small timeout to allow DOM insertion
    setTimeout(() => {
        popup.classList.add('show');
    }, 10);

    // Close logic
    const closePopup = () => {
        popup.classList.remove('show');
        setTimeout(() => {
            popup.remove(); // Remove from DOM to keep clean
        }, 300);
        localStorage.setItem('exitIntentDismissed', 'true');
    };

    closeBtn.addEventListener('click', closePopup);

    // Close on click outside
    popup.addEventListener('click', (e) => {
        if (e.target === popup) {
            closePopup();
        }
    });
};

// Initialize popup after page loads
window.addEventListener('load', () => {
    setTimeout(createEbookPopup, 1000);
});

console.log('The Wall Street Coach - Website Ready');
