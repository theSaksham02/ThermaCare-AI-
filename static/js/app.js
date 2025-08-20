// Premium ThermoVision AI Dashboard JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    initializeApp();
});

function initializeApp() {
    setupFileUpload();
    setupAnimations();
    setupLoadingStates();
    setupResponsiveBehavior();
}

function setupFileUpload() {
    const fileInput = document.getElementById('file-input');
    const uploadArea = document.querySelector('.file-upload-area');
    const form = document.querySelector('form');
    
    if (!fileInput || !uploadArea || !form) return;

    // Drag and drop functionality
    uploadArea.addEventListener('dragover', function(e) {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    });

    uploadArea.addEventListener('dragleave', function(e) {
        e.preventDefault();
        uploadArea.classList.remove('dragover');
    });

    uploadArea.addEventListener('drop', function(e) {
        e.preventDefault();
        uploadArea.classList.remove('dragover');
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            fileInput.files = files;
            handleFileSelection(files[0]);
        }
    });

    // File input change
    fileInput.addEventListener('change', function(e) {
        if (e.target.files.length > 0) {
            handleFileSelection(e.target.files[0]);
        }
    });

    // Form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        submitForm();
    });
}

function handleFileSelection(file) {
    const uploadText = document.querySelector('.upload-text');
    const uploadIcon = document.querySelector('.upload-icon');
    
    if (!uploadText || !uploadIcon) return;

    // Validate file type
    if (!file.type.startsWith('image/')) {
        showNotification('Please select an image file', 'error');
        return;
    }

    // Validate file size (max 10MB)
    const maxSize = 10 * 1024 * 1024; // 10MB
    if (file.size > maxSize) {
        showNotification('File size too large. Please select a file smaller than 10MB.', 'error');
        return;
    }

    // Update UI to show selected file
    uploadText.textContent = `Selected: ${file.name}`;
    uploadIcon.innerHTML = '📁';
    
    // Show preview if it's an image
    if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = function(e) {
            uploadIcon.innerHTML = `<img src="${e.target.result}" style="max-width: 100px; max-height: 100px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);" alt="Preview">`;
            
            // Add success notification
            showNotification('Image selected successfully!', 'success');
        };
        reader.readAsDataURL(file);
    }
}

function submitForm() {
    const form = document.querySelector('form');
    const loading = document.querySelector('.loading');
    const resultsSection = document.querySelector('.results-section');
    
    if (!form || !loading || !resultsSection) return;

    // Validate form
    const fileInput = document.getElementById('file-input');
    if (!fileInput.files.length) {
        showNotification('Please select an image file first', 'error');
        return;
    }

    // Show loading state
    loading.classList.add('show');
    resultsSection.classList.remove('show');
    
    // Add loading animation to button
    const submitButton = form.querySelector('button[type="submit"]');
    if (submitButton) {
        submitButton.innerHTML = '<span class="spinner-small"></span> Analyzing...';
        submitButton.disabled = true;
    }
    
    // Show processing notification
    showNotification('Processing thermal image...', 'info');
    
    // Hide loading after a short delay to show the animation
    setTimeout(() => {
        // Submit the form
        form.submit();
    }, 500);
}

function setupAnimations() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                
                // Add staggered animation for result cards
                if (entry.target.classList.contains('result-card')) {
                    const cards = document.querySelectorAll('.result-card');
                    cards.forEach((card, index) => {
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        }, index * 100);
                    });
                }
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    document.querySelectorAll('.result-card, .upload-section, .video-section').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Add parallax effect to header
    window.addEventListener('scroll', throttle(() => {
        const scrolled = window.pageYOffset;
        const header = document.querySelector('.header');
        if (header) {
            header.style.transform = `translateY(${scrolled * 0.1}px)`;
        }
    }, 16));
}

function setupLoadingStates() {
    // Add loading states to buttons
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', function() {
            if (this.type === 'submit') {
                this.innerHTML = '<span class="spinner-small"></span> Processing...';
                this.disabled = true;
            }
        });
    });
}

function setupResponsiveBehavior() {
    // Handle mobile menu and responsive behavior
    const handleResize = () => {
        const isMobile = window.innerWidth <= 768;
        document.body.classList.toggle('mobile', isMobile);
    };

    window.addEventListener('resize', handleResize);
    handleResize(); // Initial call
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    
    // Add icon based on type
    const icons = {
        'success': '✅',
        'error': '❌',
        'info': 'ℹ️',
        'warning': '⚠️'
    };
    
    notification.innerHTML = `
        <div class="notification-content">
            <span class="notification-icon">${icons[type] || icons.info}</span>
            <span class="notification-message">${message}</span>
            <button class="notification-close">&times;</button>
        </div>
    `;

    // Add styles with enhanced design
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'error' ? 'linear-gradient(135deg, #f56565, #e53e3e)' : 
                    type === 'success' ? 'linear-gradient(135deg, #48bb78, #38a169)' : 
                    type === 'warning' ? 'linear-gradient(135deg, #ed8936, #dd6b20)' :
                    'linear-gradient(135deg, #1a73e8, #3182ce)'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        z-index: 1000;
        transform: translateX(100%);
        transition: all 0.3s ease;
        max-width: 350px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    `;

    // Add to page
    document.body.appendChild(notification);

    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);

    // Close button functionality
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.addEventListener('click', () => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    });

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (document.body.contains(notification)) {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                if (document.body.contains(notification)) {
                    document.body.removeChild(notification);
                }
            }, 300);
        }
    }, 5000);
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Add CSS for spinner
const style = document.createElement('style');
style.textContent = `
    .spinner-small {
        display: inline-block;
        width: 16px;
        height: 16px;
        border: 2px solid rgba(255,255,255,0.3);
        border-radius: 50%;
        border-top-color: #fff;
        animation: spin 1s ease-in-out infinite;
        margin-right: 8px;
    }
    
    .notification-content {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
    }
    
    .notification-icon {
        font-size: 1.2rem;
        flex-shrink: 0;
    }
    
    .notification-message {
        flex: 1;
        font-weight: 500;
    }
    
    .notification-close {
        background: none;
        border: none;
        color: white;
        font-size: 1.2rem;
        cursor: pointer;
        margin-left: 10px;
        padding: 0;
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .notification-close:hover {
        opacity: 0.8;
    }
`;
document.head.appendChild(style);

// Export functions for global access
window.ThermoVisionAI = {
    showNotification,
    debounce,
    throttle
};
