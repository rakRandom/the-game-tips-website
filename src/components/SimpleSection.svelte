<script>
    export let className = "";
    export let title = "Título";
    export let seeAllPage = "#";
    export let elementsQt = "";
    export let innerElements = [];
    export let elementsValues = [{}];
</script>

<div class="w-full h-fit {className}">
    <div class="max-w-[1024px] h-full mx-auto">
        <div class="flex text-[#69D3C9]">
            <h2 class="text-[24px] font-medium">
                {title}
            </h2>
            <a href={seeAllPage} class="ml-auto">
                <span class="hover:underline">See All</span> &#x279C;
            </a>
        </div>
        <div class="flex justify-between mt-8">
            {#each Array(+elementsQt) as _, i}
                <svelte:component this={innerElements[i]} {...elementsValues[i]}/>
            {/each}
        </div>
    </div>
</div>

<style>
  
</style>
