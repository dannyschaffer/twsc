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
    if (localStorage.getItem('ebookPopupDismissed')) {
        return;
    }

    // Create the popup HTML
    const popupHTML = `
        <div id="ebookPopup" class="ebook-popup">
            <div class="ebook-popup-content">
                <div class="ebook-popup-text">
                    <span class="ebook-popup-icon">📚</span>
                    <div>
                        <strong>Free Trading Psychology E-Book Bundle</strong>
                        <span class="ebook-popup-subtitle">4 books on mastering your mindset — yours free</span>
                    </div>
                </div>
                <div class="ebook-popup-actions">
                    <a href="resources.html" class="ebook-popup-btn">Get Free Bundle</a>
                    <button class="ebook-popup-close" aria-label="Close popup">✕</button>
                </div>
            </div>
        </div>
    `;

    // Add CSS styles
    const popupStyles = `
        <style>
            .ebook-popup {
                position: fixed;
                bottom: -100px;
                left: 0;
                right: 0;
                background: linear-gradient(135deg, #08333A 0%, #0c464f 100%);
                color: #fff;
                z-index: 9999;
                box-shadow: 0 -4px 20px rgba(0,0,0,0.2);
                transition: bottom 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                padding: 0.75rem 1rem;
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
                gap: 1rem;
                flex-wrap: wrap;
            }
            .ebook-popup-text {
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }
            .ebook-popup-icon {
                font-size: 1.5rem;
            }
            .ebook-popup-text strong {
                display: block;
                font-size: 1rem;
                color: #C9A227;
            }
            .ebook-popup-subtitle {
                font-size: 0.85rem;
                color: rgba(255,255,255,0.7);
            }
            .ebook-popup-actions {
                display: flex;
                align-items: center;
                gap: 1rem;
            }
            .ebook-popup-btn {
                background: #C9A227;
                color: #08333A;
                padding: 0.6rem 1.5rem;
                border-radius: 50px;
                text-decoration: none;
                font-weight: 700;
                font-size: 0.9rem;
                transition: all 0.3s;
                white-space: nowrap;
            }
            .ebook-popup-btn:hover {
                background: #fff;
                transform: scale(1.05);
            }
            .ebook-popup-close {
                background: transparent;
                border: none;
                color: rgba(255,255,255,0.6);
                font-size: 1.25rem;
                cursor: pointer;
                padding: 0.25rem;
                transition: color 0.3s;
            }
            .ebook-popup-close:hover {
                color: #fff;
            }
            @media (max-width: 600px) {
                .ebook-popup-content {
                    flex-direction: column;
                    text-align: center;
                }
                .ebook-popup-text {
                    flex-direction: column;
                    gap: 0.5rem;
                }
                .ebook-popup-actions {
                    width: 100%;
                    justify-content: center;
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

    // Close button
    closeBtn.addEventListener('click', () => {
        popup.classList.remove('show');
        localStorage.setItem('ebookPopupDismissed', 'true');
    });

    // Also close when clicking the CTA (they're going to resources)
    const ctaBtn = popup.querySelector('.ebook-popup-btn');
    ctaBtn.addEventListener('click', () => {
        localStorage.setItem('ebookPopupDismissed', 'true');
    });
};

// Initialize popup after page loads
window.addEventListener('load', () => {
    setTimeout(createEbookPopup, 1000);
});

console.log('The Wall Street Coach - Website Ready');
