document.addEventListener("DOMContentLoaded", () => {
    fetch('data/sample_data.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('manhwa-container');
            data.forEach(manhwa => {
                const div = document.createElement('div');
                div.textContent = `${manhwa.title} - ${manhwa.language}`;
                container.appendChild(div);
            });
        })
        .catch(error => console.error('Error loading data:', error));
});