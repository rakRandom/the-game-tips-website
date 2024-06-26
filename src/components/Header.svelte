<script>
    export let className = "";

    let isFontBig = false;
    let userID = 100;

    $: logged = false;
    $: userDropdown = false;
    $: menuDropdown = false;

    const toggleTheme = () => {
        document.documentElement.classList.toggle('dark');
    };

    const toggleFontSize = () => {
        if (isFontBig) 
            document.documentElement.style.fontSize = "14px";
        else 
            document.documentElement.style.fontSize = "16px";
        isFontBig = !isFontBig;
    }

    const toggleMenu = () => {
        if (menuDropdown == true)
            menuDropdown = false;
        else if (menuDropdown == false)
            menuDropdown = true;
    }
</script>

<header class="z-50 bg-[#001219] w-full h-fit {className}" on:load={() => menuDropdown = false}>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js"></script>
    
    <nav class="md:max-w-[1024px] h-fit mx-auto py-2 w-full">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
            <a href="/" class="flex items-center md:space-x-3 space-x-1 rtl:space-x-reverse lg:mr-6">
                <img src="logoImage.svg" class="md:h-8 h-7" alt="Logo" />
                <span class="self-center md:text-2xl text-xl font-semibold whitespace-nowrap text-[#69D3C9]">The Game Tips</span>
            </a>
            <div class="flex flex-row items-center md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
                <button type="button" on:click={toggleTheme}> <!-- Change Theme -->
                    <img src="static/media/img/light_mode_24dp_FILL0_wght400_GRAD0_opsz24.svg" alt="Light mode" class="md:h-8 pe-3 h-4">
                </button>
                <button type="button" on:click={toggleFontSize}> <!-- Change Font Size -->
                    <img src="static/media/img/text_increase_24dp_FILL0_wght400_GRAD0_opsz24.svg" alt="Font size" class="md:h-8 pe-3 h-4">
                </button>
                <button type="button"
                    class="flex text-sm bg-gray-800 rounded-full md:me-0 ring-2"
                    class:ring-[#69D3C9]={userDropdown}
                    on:click={() => userDropdown = !userDropdown}>
                    <span class="sr-only">Open user menu</span>
                    <img class="w-8 h-8 rounded-full" src="static/media/img/profile picture placeholder.png" alt="user">
                </button>
                <!-- Dropdown menu -->
                {#if userDropdown}
                <div class="absolute top-0 translate-y-[64px] z-50 my-4 text-base list-none bg-[#001219] divide-y divide-[#69D3C9] rounded-lg shadow">
                    <div class="px-4 py-3">
                        <span class="block text-sm text-white">User Name</span>
                    </div>
                    <ul class="py-2" aria-labelledby="user-menu-button">
                        {#if logged}
                        <li>
                            <!-- 0 significa que é o próprio usuário -->
                            <a href="/#/user/0i{userID}"
                                class="block px-4 py-2 text-sm text-white hover:text-[#69D3C9]">My Account</a>
                        </li>
                        <li>
                            <a href="/"
                                class="block px-4 py-2 text-sm text-white hover:text-[#69D3C9]">Configurations</a>
                        </li>
                        <li>
                            <a href="/"
                                class="block px-4 py-2 text-sm text-white hover:text-red-600">Sign Out</a>
                        </li>
                        {:else}
                        <li>
                            <!-- 0 significa que é o próprio usuário -->
                            <a href="#/create-account"
                                class="block px-4 py-2 text-sm text-white hover:text-[#69D3C9]">Create Account</a>
                        </li>
                        <li>
                            <a href="#/login"
                                class="block px-4 py-2 text-sm text-white hover:text-[#69D3C9]">Login</a>
                        </li>
                        {/if}
                    </ul>
                </div>
                {/if}
                <button type="button" on:click={toggleMenu}
                    class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-[#69D3C9] rounded-lg md:hidden outline-none active:ring-2 active:ring-[#69D3C9]"
                    >
                    <span class="sr-only">Open main menu</span>
                    <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="#69D3C9"
                        viewBox="0 0 17 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M1 1h15M1 7h15M1 13h15" />
                    </svg>
                </button>
            </div>
            {#if (window.innerWidth >= 768 || menuDropdown)}
            <div class="items-center justify-between w-full md:flex md:w-auto md:order-1 max-md:mb-4" id="navbar-user">
                <ul
                    class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-[#69D3C9] max-md:bg-color-mid bg-transparent AAAAAAAFDF] md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0
                           max-md:text-color-body text-white *:*:block *:*:py-2 *:*:px-3 *:*:rounded max-md:divide-y max-md:dark:divide-y-2 divide-black dark:divide-white">
                    <li>
                        <a href="/"
                            class="hover:bg-[#69D3C9] hover:text-black md:hover:bg-transparent md:hover:text-[#69D3C9] md:p-0">Home</a>
                    </li>
                    <li>
                        <a href="/#/about"
                            class="hover:bg-[#69D3C9] hover:text-black md:hover:bg-transparent md:hover:text-[#69D3C9] md:p-0">About Us</a>
                    </li>
                    <li>
                        <a href="/#/help"
                            class="hover:bg-[#69D3C9] hover:text-black md:hover:bg-transparent md:hover:text-[#69D3C9] md:p-0">Help</a>
                    </li>
                </ul>
            </div>
            {/if}
            
            <div class="items-center flex lg:flex-1 lg:mx-[64px] flex-row-reverse gap-4 w-full md:w-auto md:order-1 pt-1 md:pt-0">
                <img src="static/media/img/search_24dp_FILL0_wght400_GRAD0_opsz24.svg" alt="Search" class="me-2 p-2 rounded-lg bg-color-mid border-2 dark:border border-transparent dark:hover:border-white hover:border-[#1E9B8F] active:border-[#69D3C9] dark:active:border-[#69D3C9] cursor-pointer">
                <div class="w-full relative z-0">
                    <input type="text" id="search_bar" placeholder="Search..." class="block w-full text-color-body px-2 py-2 bg-color-mid border-0 border-b-2 border-[#1E9B8F] dark:border-white appearance-none focus:outline-none focus:ring-0 focus:border-[#69D3C9] peer" />
                </div>
            </div>
        </div>
    </nav>
</header>

<style>
  
</style>
