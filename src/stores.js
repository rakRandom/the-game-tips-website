import { readable } from 'svelte/store';

const siteName = "The Game Tips";

export const title = readable((/** @type {string?} */ subtitle) => {
    if (!subtitle)
        return siteName;
    return siteName + " | " + subtitle;
});
