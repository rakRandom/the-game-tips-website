<script>
    export let legend;
    export let contents;
</script>

<div class="w-full">
    <fieldset class="text-center border-t-2 text-color-title border-[#1E9B8F]">
        <legend class="text-[1.5rem] font-title-regular px-12 hover:-translate-y-2 transition-transform select-none">{legend}</legend>
        
        <div class="grid grid-cols-1 md:grid-cols-2 grid-rows-2 gap-y-16 gap-x-16 py-12 px-[16px] xl:px-0 h-full w-full">
            {#each contents as content}
            <div>
                <h2 class="text-[2rem] font-title-medium">{content[0]}</h2>
                <p class="text-color-body break-all line-clamp-8">{content[1]}</p>
            </div>
            {/each}
        </div>
    </fieldset>
</div>
