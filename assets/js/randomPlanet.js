function fetchRandomPlanet() {
    fetch('/../data/planets.txt')
        .then(response => response.text())
        .then(data => {
            const planets = data.trim().split('\n');
            const randomPlanet = planets[Math.floor(Math.random() * planets.length)];
            document.getElementById('random-planet').textContent = randomPlanet;
        })
        .catch(error => {
            console.error('Error fetching random planet:', error);
        });
}

// Call fetchRandomPlanet function when the page is loaded
document.addEventListener('DOMContentLoaded', fetchRandomPlanet);
