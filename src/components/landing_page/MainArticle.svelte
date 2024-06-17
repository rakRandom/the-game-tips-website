<script>
    import RedirectButton from "../RedirectButton.svelte";
    
    export let className = "";

    // IMG variables
    export let src = "";
    export let alt = "";

    // Text variables
    export let gameName = "MULTIVERSUS";
    export let categoryPage = "#";
    export let articleTitle = "Bugs Bunny wins Multiversus tournament in Schick-Schick, BA";
    // Todo: Author Image
    export let authorName = "Lucas T.";
    export let articleDate = "Jun 3, 2024";
    export let authorPage = "#";  // Redirection

    // Button variables
    export let articlePage = "#";  // Redirection
</script>

<div class="bg-[#001A24] w-full h-[544px] {className}">
    <div class="flex gap-4 max-w-[1024px] h-full mx-auto py-20">
        <img {src} {alt} class="bg-white h-full aspect-video">
        <div class="flex flex-col">
            <div class="flex-1">
                <a href={categoryPage} class="text-[#69D3C9] text-[32px] font-title-semibold">
                    {gameName}
                </a>
                <p class="text-[20px] mt-4">
                    {articleTitle}
                </p>
            </div>
            
            <div class="flex items-center">
                <p class="text-[#69D3C9] text-[18px]">
                    By 
                    <a href={authorPage} class="hover:underline">
                        {authorName}
                    </a> 
                    | {articleDate}
                </p>

                <RedirectButton className="ml-auto" href={articlePage} />
            </div>
        </div>
    </div>
</div>

<style>
  
</style>
