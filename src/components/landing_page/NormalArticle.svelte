<script>
    // WARNING: Not used anymore

    export let className = "";
    export let imgSrc;
    export let gameName;
    export let title;
    export let authorPhotoSrc;
    export let authorName;
    export let postDate;
    export let articlePage;
</script>

<div class="h-[375px] min-w-[300px] {className}">
    <div class="relative w-full h-[75%]">
        <img src={imgSrc} alt="" class="h-full w-full object-cover">
        <div class="absolute w-full h-[53%] -bottom-16">
            <div class="flex w-full h-full justify-center pt-1 hover:-translate-y-1 transition-transform">
                <div class="flex flex-col text-center w-[90%] h-full bg-[#001219] rounded-md overflow-hidden cursor-pointer">
                    <div class="flex-1 py-1 px-1">
                        <h3 class="font-title-medium text-[#69D3C9] uppercase pb-1"> {gameName} </h3>
                        <p class="text-sm line-clamp-3"> {title} </p>
                    </div>
                    <a href={articlePage} class="flex items-center gap-2 text-[14px] font-light p-1 bg-[#051D26]">
                        <img src={authorPhotoSrc} alt="" class="inline-block h-6 aspect-square border-[1px] border-[#69D3C9BE] rounded-full">
                        <span class="text-[#69D3C9BE] w-full text-center">By {authorName} - {postDate}</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
  
</style>

