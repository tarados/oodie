export function fontSize(screenCurrent, fontSizeMin, fontSizeMax, screenMax, screenMin) {
    return ((screenCurrent - screenMin) / (screenMax - screenMin)) * (fontSizeMax - fontSizeMin) + fontSizeMin
}


