<script>
    export let className = "";

    let foo = "hidden";

    let show = () => {foo = ""};

    let hide = () => {foo = "hidden"};
</script>

<div class="h-[90px] w-[90px] bg-white rounded-full hover:cursor-pointer hover:-translate-y-1 transition-transform {className}">
    <button type="button" on:click={show} class="w-full h-full rounded-full">
        
    </button>
</div>

<div class="{foo} fixed z-50 top-0 left-0 w-screen h-screen bg-[#00000010]">
    <div class="flex items-center justify-center h-full w-full">
        <div class="w-[300px] h-[400px] bg-white">
            <button type="button" on:click={hide} class="w-[30px] h-[30px] p-2 bg-black">X</button>
        </div>
    </div>
</div>

<style>
  
</style>
