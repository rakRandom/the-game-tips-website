<script>
    import RedirectButton from "../RedirectButton.svelte";
    
    export let className = "";

    // IMG variables
    export let imgSrc = "";

    // Text variables
    export let gameName;
    export let categoryPage;
    export let articleTitle;
    // Todo: Author Image
    export let authorName;
    export let articleDate;
    export let authorPage;  // Redirection

    // Button variables
    export let articlePage;  // Redirection
</script>

<div class="bg-[#001A24] w-full h-[544px] {className}">
    <div class="flex gap-4 max-w-[1024px] h-full mx-auto py-20">
        <img src={imgSrc} alt="" class="bg-white h-full aspect-video">
        <div class="flex flex-col">
            <div class="flex-1">
                <a href={categoryPage} class="group text-[#69D3C9] text-[2rem] font-title-semibold uppercase cursor-pointer">
                    {gameName}
                    <hr class="w-0 transition-all delay-100 duration-1000 border-[1px] border-transparent group-hover:border-[#69D3C9] group-hover:w-full">
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
