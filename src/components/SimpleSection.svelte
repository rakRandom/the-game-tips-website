<script>
    export let className = "";
    export let title = "Título";
    export let seeAllPage = "#";
    export let innerElements = [];
</script>

<div class="w-full h-fit {className}">
    <div class="max-w-[1024px] h-full mx-auto">
        <div class="flex text-[#69D3C9]">
            <h2 class="text-[24px]">
                {title}
            </h2>
            <a href={seeAllPage} class="ml-auto">
                <span class="hover:underline">See All</span> &#x21FE; &#x2794; &#x279C;
            </a>
        </div>
        <div class="flex justify-between mt-8">
            {#each innerElements as element}
                <svelte:component this={element}/>
            {/each}
        </div>
    </div>
</div>

<style>
  
</style>
