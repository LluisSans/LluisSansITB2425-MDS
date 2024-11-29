document.addEventListener("DOMContentLoaded", () => {
    // Selecciona todas las imágenes dentro de las secciones
    const images = document.querySelectorAll("section.about-me img");

    // Añade un evento de mouseover para cada imagen
    images.forEach((img) => {
        img.addEventListener("mouseover", () => {
            img.style.transform = "scale(1.1)"; // Aumenta ligeramente el tamaño
            img.style.transition = "transform 0.3s ease-in-out"; // Transición suave
        });

        img.addEventListener("mouseout", () => {
            img.style.transform = "scale(1)"; // Restaura el tamaño original
        });

        // Añade un evento de clic para girar la imagen
        img.addEventListener("click", () => {
            img.style.transform = "rotate(360deg)";
            img.style.transition = "transform 0.5s ease-in-out";
            setTimeout(() => {
                img.style.transform = "scale(1)";
            }, 500); // Restaura el estado tras completar la rotación
        });
    });
});