const CACHE_NAME = 'dayrut-65km-v2026.11.10';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './project_data.json',
  './pricing_data.json',
  './letters_data.json',
  './manifest.json',
  './icon.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((k) => {
          if (k !== CACHE_NAME) {
            console.log('Removing old cache:', k);
            return caches.delete(k);
          }
        })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  const url = e.request.url;
  
  // Never cache PDF files or API calls - always direct from network/disk
  if (url.includes('.pdf') || url.includes('.PDF') || url.includes('/api/') || url.includes('/%D8%A7%D9%84%D9%85%D8%B1%D8%A7%D8%B3%D9%84%D8%A7%D8%AA/')) {
    e.respondWith(fetch(e.request));
    return;
  }

  // Network-first strategy with cache fallback for app assets
  e.respondWith(
    fetch(e.request)
      .then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(e.request, responseToCache);
          });
        }
        return networkResponse;
      })
      .catch(() => caches.match(e.request))
  );
});
