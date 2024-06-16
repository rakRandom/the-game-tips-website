<script>
    export let className = "";

    export let name;
    export let phrase;
    export let articlePage = "#";

    let foo = "hidden";
    let show = () => {foo = "";};
    let hide = () => {foo = "hidden";};
</script>

<div class="flex flex-col items-center 
            min-h-[90px] w-[100px] 
            hover:cursor-pointer hover:-translate-y-1 
            transition-transform {className}"
    >
    <button type="button" on:click={show} class="flex items-center justify-center w-[90px] h-[90px] rounded-full
                                                 bg-gradient-to-tr from-[#2EC4B6] to-[#FF2202]"
            >
            <div class="w-[82px] h-[82px] rounded-full bg-white"></div>
    </button>

    <h1 class="text-center text-[#69D3C9] h-fit break-words">
        {name}
    </h1>
</div>

<div class="{foo} fixed z-50 top-0 left-0 w-screen h-screen bg-[#00000020] backdrop-blur-sm">
    <div class="flex flex-col gap-4 items-center justify-center h-full w-full">
        <div class="relative w-[380px] h-[560px] bg-white rounded-xl overflow-hidden">
            <button type="button" on:click={hide} 
                class="absolute top-2 right-2 w-[30px] h-[30px] pb-[1px] bg-[#000000A0] rounded-full opacity-75 hover:opacity-100">
                X
            </button>
            
            <div class="flex items-end h-full w-full">
                <div class="bg-[#000000A0] min-h-[100px] w-full px-4 py-2">
                    {phrase}
                </div>
            </div>
        </div>
        <div>
            <a href={articlePage} class="group text-black">
                Want to see more? Check out the complete tip ;)
                <hr class="w-0 mx-auto border-black 
                           group-hover:w-[75%]
                           transition-all duration-500">
            </a>
        </div>
    </div>
</div>

<style>
  
</style>
