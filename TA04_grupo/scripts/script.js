document.addEventListener('DOMContentLoaded', function() {
    // Animación para el título
    var h1Element = document.querySelector('h1');
    var title = h1Element.innerText;
    var animatedTitle = '';

    let index = 0;
    function animateTitle() {
        if (index < title.length) {
            animatedTitle += title[index];
            h1Element.innerText = animatedTitle;
            index++;
            setTimeout(animateTitle, 150);
        }
    }

    animateTitle();
});