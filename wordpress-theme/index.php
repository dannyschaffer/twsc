<?php
get_header();
?>

<div class="container" style="padding-top: 120px; padding-bottom: 60px;">
    <?php
    if ( have_posts() ) :
        while ( have_posts() ) : the_post();
            ?>
            <div class="page-content">
                <h1><?php the_title(); ?></h1>
                <?php the_content(); ?>
            </div>
            <?php
        endwhile;
    else :
        echo '<p>No content found</p>';
    endif;
    ?>
</div>

<?php
get_footer();
?>
