<?php
/**
 * Template Name: Resources Page
 */

get_header();
?>

    <style>
        .book-showcase {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
            background: #fff;
            padding: 4rem;
            border-radius: 12px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
            margin: 5rem 0;
            position: relative;
            z-index: 10;
        }

        .book-image img {
            width: 100%;
            max-width: 450px;
            box-shadow: 10px 10px 30px rgba(0, 0, 0, 0.15);
            transition: transform 0.3s ease;
            border-radius: 8px;
        }

        .book-image img:hover {
            transform: scale(1.02);
        }

        .free-tool-card {
            background: #F9F9F7;
            border: 1px solid rgba(0, 0, 0, 0.05);
            padding: 1.5rem;
            border-radius: 12px;
            transition: transform 0.3s ease, border-color 0.3s ease;
            text-align: left;
        }

        .free-tool-card:hover {
            transform: translateY(-5px);
            border-color: var(--gold);
        }

        .free-tool-card img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 1rem;
        }

        /* Generic card styles */
        .ebook-card {
            background: #fff;
            border: 1px solid rgba(0, 0, 0, 0.08);
            padding: 1.5rem;
            border-radius: 12px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            text-align: left;
            position: relative;
            overflow: hidden;
        }

        .ebook-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 1rem;
        }

        /* Locked State */
        .ebook-card.locked {
            opacity: 1; /* Keep full opacity but overlay covers it */
            cursor: pointer;
        }
        
        .ebook-card.locked img, 
        .ebook-card.locked h3, 
        .ebook-card.locked p,
        .ebook-card.locked span {
            opacity: 0.5;
            transition: opacity 0.3s;
        }

        .lock-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(8, 51, 58, 0.05); /* Tint */
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0.8; /* Visible by default to show lock */
            transition: all 0.3s ease;
            z-index: 5;
        }

        .ebook-card.locked:hover .lock-overlay {
            background: rgba(8, 51, 58, 0.85); /* Darken on hover */
            opacity: 1;
        }

        .lock-content {
            text-align: center;
            color: var(--navy);
            transform: translateY(0);
            transition: transform 0.3s;
        }
        
        .ebook-card.locked:hover .lock-content {
            color: #fff;
        }

        .lock-icon svg {
            width: 40px;
            height: 40px;
            fill: var(--navy);
            margin-bottom: 0.5rem;
            transition: fill 0.3s;
        }
        
        .ebook-card.locked:hover .lock-icon svg {
            fill: var(--gold);
        }

        .unlock-text {
            font-family: 'Space Mono', monospace;
            text-transform: uppercase;
            font-weight: 700;
            font-size: 0.9rem;
            letter-spacing: 1px;
            opacity: 0; /* Hidden initially, show on hover */
            transform: translateY(10px);
            transition: all 0.3s;
        }

        .ebook-card.locked:hover .unlock-text {
            opacity: 1;
            transform: translateY(0);
        }

        .resources-grid, .ebooks-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }

        /* Live Coaching Styles */
        .live-coaching-section {
            padding-bottom: 5rem;
        }
        
        .live-coaching-header-bar {
            background-color: var(--green-tint);
            padding: 4rem 0;
            margin: 0 0 3rem 0; 
            width: 100%;
            text-align: center;
        }
        
        .live-coaching-header-bar h2 {
            color: var(--navy);
            margin-bottom: 1rem;
        }
        
        .live-coaching-header-bar p {
             color: var(--text-secondary);
             max-width: 600px; 
             margin: 0 auto;
        }

        .video-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }
        .video-card {
            background: #fff;
            border-radius: 12px;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            border: 1px solid rgba(0,0,0,0.05);
            transition: transform 0.3s ease;
        }
        .video-card:hover {
            transform: translateY(-5px);
        }
        /* ... (Video styles same as before) ... */
        .video-thumbnail { position: relative; padding-bottom: 56.25%; background: #000; overflow: hidden; }
        .video-thumbnail img { position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; opacity:0.95; }
        .play-icon { position: absolute; top:50%; left:50%; transform: translate(-50%,-50%); width:60px; height:60px; background:rgba(8,51,58,0.8); border-radius:50%; display:flex; align-items:center; justify-content:center; border:2px solid #fff; }
        .play-icon svg { fill:#fff; margin-left:4px; }
        .video-info { padding: 1.5rem; }
        .video-title { font-family: 'Inter', sans-serif; font-weight:600; font-size:1.1rem; color:var(--navy); margin:0; }

        /* Modal */
        .video-modal { display: none; position: fixed; z-index: 9999; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(8, 51, 58, 0.95); align-items: center; justify-content: center; backdrop-filter: blur(5px); }
        .modal-content { position: relative; width: 90%; max-width: 900px; background: #000; padding: 0; border-radius: 12px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); overflow: hidden; }
        .close-modal { position: absolute; top: -40px; right: 0; color: #fff; font-size: 40px; cursor: pointer; }
        .modal-video-wrapper { position: relative; padding-bottom: 56.25%; height: 0; }
        .modal-video-wrapper iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
        #modalTitle { color: #fff; padding: 1.5rem; background: #111; text-align: center; margin: 0; }
        
        .load-more-container { text-align: center; margin-top: 3rem; }
        .btn-secondary-load { background: transparent; border: 1px solid var(--navy); color: var(--navy); padding: 1rem 2.5rem; cursor: pointer; font-family: 'Space Mono', monospace; text-transform: uppercase; }

        @media (max-width: 768px) {
            .book-showcase { grid-template-columns: 1fr; text-align: center; padding: 2rem; }
        }
    </style>

    <section class="section" style="padding-top: 2rem;">
        <div class="container">

            <!-- 1. Free Tools & Diagnostics (Unlocked) -->
            <div style="margin-bottom: 5rem;">
                <h2 style="text-align: center; margin-bottom: 3rem; color: var(--navy);">Free Tools & Diagnostics</h2>
                <div class="resources-grid">
                    <!-- Quiz -->
                    <div class="free-tool-card">
                        <img src="<?php echo get_template_directory_uri(); ?>/assets/images/cover-quiz.png" alt="Quiz"> 
                        <h3 style="color: var(--navy);">Attached to the Trade Quiz</h3>
                        <p style="font-size: 0.9rem; color: var(--text-secondary);">Discover your specific "Trader Archetype".</p>
                        <a href="https://attachedtothetrade.com/" target="_blank" style="color: var(--gold); font-weight: 700;">Take Quiz →</a>
                    </div>
                    
                    <!-- Universal Needs Matrix -->


                    <!-- Trader Hero's Journey -->
                     <div class="free-tool-card">
                        <img src="<?php echo get_template_directory_uri(); ?>/assets/images/cover-hero-journey.png" alt="Journey">
                        <h3 style="color: var(--navy);">Trader Hero's Journey</h3>
                        <p style="font-size: 0.9rem; color: var(--text-secondary);">Map your career lifecycle.</p>
                        <a href="https://coachingproducts.s3.us-east-2.amazonaws.com/Trading+Hero's+Journey+Map.pdf" target="_blank" style="color: var(--gold); font-weight: 700;">Download PDF →</a>
                    </div>

                    <!-- Trader Check-In -->
                     <div class="free-tool-card">
                        <img src="<?php echo get_template_directory_uri(); ?>/assets/images/cover-trader-checkin.png" alt="Check-In">
                        <h3 style="color: var(--navy);">Trader Check-In</h3>
                        <p style="font-size: 0.9rem; color: var(--text-secondary);">Daily psychology worksheet.</p>
                        <a href="https://coachingproducts.s3.us-east-2.amazonaws.com/TWSC+Trader+Check-In.pdf" target="_blank" style="color: var(--gold); font-weight: 700;">Download PDF →</a>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- 2. Kim's Book Header & Section -->
    <section class="section" style="padding-top: 0; padding-bottom: 0;">
        <div class="live-coaching-header-bar" style="margin-bottom: 0;">
            <div class="container">
                <h2 style="color: var(--navy); margin-bottom: 0;">Kim's Book</h2>
            </div>
        </div>
        <div class="container">
            <div class="book-showcase" style="margin-top: 3rem;">
                <div class="book-image">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/transforming-ws-book.png" alt="Book Cover">
                </div>
                <div class="book-content">
                    <span style="color: var(--gold); font-family: 'Space Mono'; text-transform: uppercase;">The Bestseller</span>
                    <h2 style="font-size: 2.5rem; margin: 1rem 0; color: var(--navy);">Transforming Wall Street</h2>
                    <p style="margin-bottom: 1.5rem; color: var(--text-secondary);">I interviewed 50 legendary traders and investors to decode the DNA of sustainable success.</p>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <a href="https://www.amazon.com/Transforming-Wall-Street-Conscious-Future/dp/1940984599" target="_blank" class="btn-primary">Get the Book</a>
                    </div>
                </div>
            </div>

            <!-- 3. The 5 Practices E-Book (LOCKED - Lead Capture) -->
            <div style="margin-bottom: 2rem; margin-top: 5rem; max-width: 600px; margin-left: auto; margin-right: auto;">
                <h2 style="text-align: center; margin-bottom: 3rem; color: var(--navy);">Trading Psychology E-Book</h2>
                <div class="ebooks-grid" style="grid-template-columns: 1fr;">
                    <!-- LINK TO THE LEAD CAPTURE PAGE -->
                    <div class="ebook-card locked" onclick="window.location.href='<?php echo site_url('/download'); ?>'" style="text-align: center;">
                        <div class="lock-overlay">
                            <div class="lock-content">
                                <div class="lock-icon">
                                    <svg viewBox="0 0 24 24"><path d="M12 17c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm6-9h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zM9 6c0-1.66 1.34-3 3-3s3 1.34 3 3v2H9V6z"/></svg>
                                </div>
                                <div class="unlock-text">Unlock Free</div>
                            </div>
                        </div>
                        <img src="<?php echo get_template_directory_uri(); ?>/assets/images/5-practices-tools.jpg" alt="The 5 Practices to Become a Better Trader" style="height: 350px; width: auto; max-width: 100%; margin: 0 auto 1rem;">
                        <h3 style="color: var(--navy); margin: 0.5rem 0;">The 5 Practices to Become a Better Trader</h3>
                        <p style="font-size: 0.9rem; color: var(--text-secondary);">Simple "Brain Hacks" to overcome roadblocks.</p>
                    </div>
                </div>
            </div>

        </div> 
    </section>

    <!-- 4. Live Coaching Section -->
    <section class="live-coaching-section">
        <div class="live-coaching-header-bar">
            <div class="container">
                <h2 style="color: var(--navy); margin-bottom: 1rem;">Live Coaching Library</h2>
                <p style="color: var(--text-secondary);">Watch Kim Ann Curtin coach traders in real-time.</p>
            </div>
        </div>
        <div class="container">
            <div id="videoGrid" class="video-grid"></div>
            <div class="load-more-container"><button id="loadMoreBtn" class="btn-secondary-load">Load More Videos</button></div>
        </div>
    </section>

<!-- Video Modal & Script -->
<div id="videoModal" class="video-modal">
    <div class="modal-content">
        <span class="close-modal">&times;</span>
        <div class="modal-video-wrapper"><iframe id="modalIframe" src="" frameborder="0" allowfullscreen></iframe></div>
        <h3 id="modalTitle"></h3>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // ... Same Video JS ...
    const grid = document.getElementById('videoGrid');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const modal = document.getElementById('videoModal');
    const modalIframe = document.getElementById('modalIframe');
    const modalTitle = document.getElementById('modalTitle');
    const closeModal = document.querySelector('.close-modal');
    
    let videos = [];
    let displayed = 0;
    const BATCH_SIZE = 8; 

    // Use Safer PHP path injection
    fetch('<?php echo get_template_directory_uri(); ?>/live-coaching.json')
        .then(response => response.json())
        .then(data => {
            videos = data;
            renderVideos();
        })
        .catch(err => console.error('Error loading videos:', err));

    function renderVideos() {
        if (!videos.length) return;
        const nextBatch = videos.slice(displayed, displayed + BATCH_SIZE);
        nextBatch.forEach(video => {
            const card = document.createElement('div');
            card.className = 'video-card';
            card.innerHTML = `
                <div class="video-thumbnail">
                    <img src="https://img.youtube.com/vi/${video.videoId}/hqdefault.jpg">
                    <div class="play-icon"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></div>
                </div>
                <div class="video-info"><h3 class="video-title">${video.title}</h3></div>`;
            card.addEventListener('click', () => openModal(video));
            grid.appendChild(card);
        });
        displayed += nextBatch.length;
        if (displayed >= videos.length && loadMoreBtn) loadMoreBtn.style.display = 'none';
    }
    if(loadMoreBtn) loadMoreBtn.addEventListener('click', renderVideos);
    function openModal(video) {
        modalIframe.src = `https://www.youtube.com/embed/${video.videoId}?autoplay=1`;
        modalTitle.textContent = video.title;
        modal.style.display = 'flex';
    }
    function closeModalFunc() { modal.style.display = 'none'; modalIframe.src = ''; }
    if(closeModal) closeModal.addEventListener('click', closeModalFunc);
    window.addEventListener('click', (e) => { if (e.target == modal) closeModalFunc(); });
});
</script>

<?php get_footer(); ?>
