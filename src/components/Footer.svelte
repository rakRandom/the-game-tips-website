<script>
    export let className = "";

    let games = [
        "Minecraft",
        "Survival Games",
        "Horror",
        "Elden Ring",
        "Genshin Impact",
        "Red Dead Redemption 2",
        "Roblox",
        "Playstation",
        "Multiversus",
        "Plants vs Zombies",
        "Pokemon Black",
        "Dragon Ball: Kakarot",
    ]

    let routes = [
        ["/#/login", "Login"],
        ["/#/sigin", "Sign In"],
        ["/#/about", "About Us"],
        ["/#/help", "Help"],
        ["https://github.com/rakRandom/dicas-de-jogos-site", "Community"],
    ];
</script>

<footer class="flex flex-col bg-[#00141E] text-white w-full lg:max-h-[340px] {className} *:w-full *:*:mx-auto *:*:max-w-[1024px]">
    <div class="h-full lg:h-[260px]">
        <div class="flex flex-col lg:flex-row w-full h-full mx-auto py-4 *:h-full">
            <div class="flex-1 pb-8 flex flex-col px-[16px] sm:px-[32px] lg:px-0 lg:pl-[32px] xl:pl-0">
                <h2 class="text-[1.75rem] font-title-semibold text-[#2EC4B6] mb-2 cursor-pointer hover:translate-x-2 transition-transform">
                    <a href="/">
                        The Game Tips
                    </a>
                </h2>
                <p class="text-[1.2rem] mb-4">
                    Helping the gamers with their seek for Tips and Treasures all around the world!
                </p>
                <div class="flex-1 flex gap-4 items-end">
                    <a href="/"><img src="static/media/img/icons8-whatsapp.svg" alt="WhatsApp" class="h-8 w-8" /></a>
                    <a href="/"><img src="static/media/img/icons8-twitterx.svg" alt="Twitter" class="h-8 w-8" /></a>
                    <a href="/"><img src="static/media/img/icons8-facebook-novo.svg" alt="Facebook" class="h-8 w-8" /></a>
                </div>
            </div>

            <div class="hidden lg:block w-[1px] border"></div>
            <hr class="block lg:hidden mx-[16px] sm:mx-[32px] mb-6">

            <div class="flex-1 px-[16px] sm:px-[32px] lg:px-0 lg:pl-12 pb-8">
                <h2 class="text-[1.75rem] font-title-semibold text-[#2EC4B6] mb-2 cursor-pointer hover:translate-x-2 transition-transform">
                    More Hints
                </h2>
                <div class="flex flex-col flex-wrap h-full max-md:h-[150px] max-lg:h-[100px] overflow-hidden *:w-fit hover:*:underline hover:*:translate-x-1 *:transition-transform">
                    {#each games as game}
                        <a href="/">{game}</a>
                    {/each}
                </div>
            </div>
        </div>
  </div>

    <div class="flex items-center h-[80px] bg-[#001B28] border-t-[5px] border-[#002331]">
        <div class="flex items-center w-full h-full mx-auto sm:px-[32px] xl:px-0">
            <a href="/" class="h-12">
                <img src="logoImage.svg" alt="" class="hidden sm:block h-full" />
            </a>
            
            <div class="relative w-full h-full">
                <div class="absolute w-full h-full top-0">
                    <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-10 h-full w-full text-[1.1rem] text-[#69D3C9] hover:*:underline">
                        {#each routes as route}
                            <a href={route[0]}>{route[1]}</a>
                        {/each}
                    </div>
                </div>
            </div>
        </div>
    </div>
</footer>
