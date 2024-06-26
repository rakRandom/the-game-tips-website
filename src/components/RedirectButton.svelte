<script>
    export let className = "";
    export let value = "Read more";
    export let href = "#";

    href = "#/category/" + href;
</script>

<a {href} class="flex items-center justify-center w-[120px] h-[48px] bg-[#2EC4B6] rounded {className}">
    <span class="text-color-body font-bold">
        {value}
    </span>
</a>

<style>
  
</style>
