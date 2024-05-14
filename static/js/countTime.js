function getCurrentTime() {
    let now = new Date();
    let year = now.getFullYear();
    let month = String(now.getMonth() + 1).padStart(2, '0');
    let day = String(now.getDate()).padStart(2, '0');
    let hour = String(now.getHours()).padStart(2, '0');
    let minute = String(now.getMinutes()).padStart(2, '0');
    let second = String(now.getSeconds()).padStart(2, '0');
    
    return `${year}-${month}-${day} ${hour}:${minute}:${second}`;
}

function updateCurrentTime() {
    let currentTimeElement = document.getElementById('currentTime');
    if (currentTimeElement) {
        let currentTime = getCurrentTime();
        currentTimeElement.textContent = currentTime;
    }

    // Set timeout for next update (every second)
    setTimeout(updateCurrentTime, 1000);
}

// Initial call to start updating time
updateCurrentTime();
