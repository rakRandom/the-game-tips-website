<script>
    import { fly } from "svelte/transition";
    import { fetchImage } from "../../api/api_connection";

    // Game - Title - Src - Href
    export let contents;

    let visible = 0;
    let href = contents[0][3];
    let src = contents[0][2];

    const changeItem = (/** @type {number} */ key) => { 
        visible = key; 
        href = contents[key][3];
        src = contents[key][2];

        clearInterval(interval);
        interval = setInterval(() => {
            changeItem((visible == contents.length - 1) ? 0 : visible + 1);
        }, 5000);
    }

    let interval = setInterval(() => {
        changeItem((visible == contents.length - 1) ? 0 : visible + 1);
    }, 5000);

    setTimeout(() => { changeItem(0) }, 500)
</script>

<div class="h-fit lg:h-[500px] w-full">
    <div class="flex flex-col lg:flex-row gap-6 h-full max-w-[1024px] mx-auto">
        <div class="h-full aspect-square sm:aspect-[15/10] overflow-hidden cursor-pointer lg:rounded-lg">
            <div class="relative h-full w-full">
                <a href={"#/article/" + href} class="absolute h-full w-full"><span></span></a>
                <img src={fetchImage(src)} alt="" class="absolute h-full w-full object-cover">
                {#each contents as content, i}
                    {#if visible == i}
                        <div class="z-20 flex items-end h-full w-full">
                            <div class="relative h-fit w-full px-4 py-8 text-black bg-gradient-to-b from-[#2EC4B600] to-[#2EC4B65A] backdrop-blur-[4px]">
                                <div in:fly={{y: 200, duration: 1000, delay: 1000}} out:fly={{y:-200, duration:750}}>
                                    <!-- This text needs to be only one color -->
                                    <h2 class="text-[2rem] text-[#69D3C9] uppercase font-title-bold">
                                        {content[0]}
                                    </h2>
                                    <!-- This text needs to be only white -->
                                    <p class="text-[1.5rem] text-white mt-2"> 
                                        {content[1]}
                                    </p>
                                </div>
                            </div>
                        </div>
                    {/if}
                {/each}
            </div>
        </div>

        <div class="hidden sm:block lg:flex-1">
            <ul class="flex lg:flex-col gap-4 h-full px-[16px] lg:px-0 *:flex-1 *:bg-color-mid *:rounded-lg *:overflow-hidden">
                {#each contents as content, i}
                <li data-key={i} class="sm:hover:translate-y-1 lg:hover:translate-y-0 lg:hover:translate-x-1 transition all">
                    <button on:click={() => changeItem(i)} class="flex flex-col gap-2 lg:flex-row items-center h-full w-full">
                        <img src={fetchImage(content[2])} alt="" class="h-full aspect-square object-cover">
    
                        <div class="text-sm text-color-title text-left h-full lg:h-fit pt-1 break-words p-2">
                            {content[1]}
                        </div>
                    </button>
                </li>
                {/each}
            </ul>
        </div>
    </div>
</div>

<style>
    
</style>
