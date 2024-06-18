import { readable, writable, get } from 'svelte/store';

//
const siteName = "The Game Tips";

export const title = readable((/** @type {string?} */ subtitle) => {
    if (!subtitle)
        return siteName;
    return siteName + " | " + subtitle;
});
//

//
const fontSizes = [
    12,
    20,
    32,
];

export let isFontBig = writable(false);

export const getFontSize = readable((/** @type {number} */ sizeNumber) => {
    if (sizeNumber < 0 || sizeNumber > fontSizes.length)
        return "";
    
    return `text-[${fontSizes[sizeNumber] * ((get(isFontBig)) ? 2 : 1)}px]`;
});
//
