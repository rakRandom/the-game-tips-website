<script>
    export let gamename="Multiversus", gameimage = "", gamelink = "";
</script>

<div>
    <a href="{gamelink}" class="flex flex-row bg-color-mid w-full rounded-3xl overflow-hidden hover:-translate-y-2 duration-75">
        <img class="w-20 aspect-square" src="{gameimage}">
        <p class="my-auto mx-5 md:text-xl text-lg text-color-body break-words">{gamename}</p>
    </a>
</div>

<style>

</style>