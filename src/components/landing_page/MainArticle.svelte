<script>
    import { fetchImage } from "./../../api/api_connection";
    
    export let className = "";

    // IMG variables
    export let imgSrc;

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

<div class="bg-[#001A24] w-full h-fit {className}">
    <div class="flex flex-col gap-8 max-w-[1280px] mx-auto pb-10 lg:pt-10 lg:px-[64px] h-full">
        <a href={articlePage} class="aspect-video">
            <img src={fetchImage(imgSrc)} alt="" class="h-full w-full aspect-video object-cover lg:rounded-xl">
        </a>
        
        <div class="flex flex-col-reverse lg:flex-row gap-4 w-full px-[16px] lg:px-[32px]">
            <div class="w-full lg:w-[280px] text-[#1E9B8F] dark:text-[#69D3C9]">
                <h2 class="text-[2rem] font-title-medium uppercase">
                    <a href={categoryPage}>
                        {gameName}
                    </a>
                </h2>
                <p class="opacity-75 font-light">
                    By
                    <a href={authorPage}>
                        {authorName}
                    </a>
                    - {articleDate}
                </p>
            </div>
            <div class="flex items-center w-full dark:bg-[#051D26] px-4 py-2 rounded-lg">
                <a href={articlePage} class="text-[1rem] lg:text-[1.5rem] w-full hover:pl-2 transition-all">
                    {articleTitle}
                </a>
            </div>
        </div>
    </div>
</div>

<style>
  
</style>
