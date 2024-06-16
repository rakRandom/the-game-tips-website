<script>
    import RedirectButton from '../RedirectButton.svelte'

    export let foo = [
        ["", "", "YO BRO COME OVER HERE COME OVER HERE CHECK OUT MY NEW SHOES"],
        ["", "", "A"],
        ["", "", "A"],
        ["", "", "A"],
        ["", "", "A"]
    ];

    // Todo: Dynamic modification of this variables
    let currentGame = "";
    let description = "";
    let articlePage = "";
</script>

<div class="h-[500px] w-full">
    <div class="flex gap-6 h-full max-w-[1024px] mx-auto">
        <div class="flex items-end h-full aspect-[15/10] rounded-lg bg-white overflow-hidden">
            <div class="h-[50%] w-full p-4 pt-24 text-black
                        bg-gradient-to-b from-[#00103000] to-[#001030AA]">
                <h2 class="text-3xl text-cyan-300">
                    {currentGame}
                </h2>
                <p>
                    {description}
                </p>
                <RedirectButton href={articlePage} />
            </div>
        </div>
        <div class="flex-1 flex flex-col gap-4 h-full ">
            {#each foo as bar}
                <div class="flex gap-4 items-center flex-1 bg-white rounded-lg overflow-hidden">
                    <img src={bar[0]} alt={bar[1]} class="h-full aspect-square">

                    <div class="text-sm text-black break-words">
                        {bar[2]}
                    </div>
                </div>
            {/each}
        </div>
    </div>
</div>

<style>

</style>
