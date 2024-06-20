import { get } from "svelte/store";
import { apiLink } from "../stores";

/**
 * @param {string} request
 * @param {RequestInit | null} body
 */
async function requestApi(request, body) {
    let link = get(apiLink);

    if (body)
        return await fetch(`${link}/${request}`, body);
    return await fetch(`${link}/${request}`);
}

async function fetchImage(path) {
    if (!path)
        return;

    let link = get(apiLink);
    return await fetch(`${link}/${path}`);
}

export { requestApi, fetchImage as getImage };
