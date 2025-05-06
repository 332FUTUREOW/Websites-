const manhwaData = [
  {
    title: "Solo Leveling",
    chapters: 179,
    image: "https://example.com/solo-leveling.jpg",
  },
  {
    title: "Tower of God",
    chapters: 550,
    image: "https://example.com/tower-of-god.jpg",
  },
  {
    title: "The Beginning After the End",
    chapters: 200,
    image: "https://example.com/beginning.jpg",
  },
];

// توليد محتوى المانهوا وعرضه في الصفحة
const manhwaList = document.getElementById("manhwa-list");

manhwaData.forEach((manhwa) => {
  const manhwaItem = document.createElement("div");
  manhwaItem.className = "manhwa-item";
  manhwaItem.innerHTML = `
    <img src="${manhwa.image}" alt="${manhwa.title}" />
    <h3>${manhwa.title}</h3>
    <p>Chapters: ${manhwa.chapters}</p>
  `;
  manhwaList.appendChild(manhwaItem);
});
