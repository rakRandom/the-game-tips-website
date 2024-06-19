<script>
    export let className = "";

    let isFontBig = false;

    const toggleTheme = () => {
        document.documentElement.classList.toggle('dark');
    };

    const toggleFontSize = () => {
        if (isFontBig) 
            document.documentElement.style.fontSize = "15px";
        else 
            document.documentElement.style.fontSize = "17px";
        isFontBig = !isFontBig;
    }
</script>

<header class="z-50 dark:bg-[#001219] bg-[#DFDFDF] w-full md:h-[80px] h-[110px] {className}">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js"></script>
    
    <nav class="md:max-w-[1024px] h-full mx-auto py-2 w-full">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
            <a href="/" class="flex items-center md:space-x-3 space-x-1 rtl:space-x-reverse">
                <img src="public\logoImage.svg" class="md:h-8 h-7" alt="Logo" />
                <span class="self-center md:text-2xl text-xl font-semibold whitespace-nowrap text-[#69D3C9]">The Game Tips</span>
            </a>
            <div class="flex flex-row items-center md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
                <button type="button" on:click={toggleTheme}> <!-- Change Theme -->
                    <img src="src\assets\img\light_mode_24dp_FILL0_wght400_GRAD0_opsz24.svg" alt="Light mode" class="md:h-8 pe-3 h-4">
                </button>
                <button type="button" on:click={toggleFontSize}> <!-- Change Font Size -->
                    <img src="src\assets\img\text_increase_24dp_FILL0_wght400_GRAD0_opsz24.svg" alt="Font size" class="md:h-8 pe-3 h-4">
                </button>
                <button type="button"
                    class="flex text-sm bg-gray-800 rounded-full md:me-0 focus:ring-4 focus:ring-[#69D3C9]"
                    id="user-menu-button" aria-expanded="false" data-dropdown-toggle="user-dropdown"
                    data-dropdown-placement="bottom">
                    <span class="sr-only">Open user menu</span>
                    <img class="w-8 h-8 rounded-full" src="src\assets\img\profile picture placeholder.png" alt="user">
                </button>
                <!-- Dropdown menu -->
                <div class="z-50 hidden my-4 text-base list-none dark:bg-[#001219] bg-[#DFDFDF] divide-y divide-[#69D3C9] rounded-lg shadow"
                    id="user-dropdown">
                    <div class="px-4 py-3">
                        <span class="block text-sm dark:text-white text-black">User Name</span>
                    </div>
                    <ul class="py-2" aria-labelledby="user-menu-button">
                        <li>
                            <a href="/#/user/:id"
                                class="block px-4 py-2 text-sm dark:text-white text-black hover:text-[#69D3C9]">My Account</a>
                        </li>
                        <li>
                            <a href="/"
                                class="block px-4 py-2 text-sm dark:text-white text-black hover:text-[#69D3C9]">Configurations</a>
                        </li>
                        <li>
                            <a href="/"
                                class="block px-4 py-2 text-sm dark:text-white text-black hover:text-red-600">Sign Out</a>
                        </li>
                    </ul>
                </div>
                <button data-collapse-toggle="navbar-user" type="button"
                    class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-[#69D3C9] rounded-lg md:hidden focus:outline-none focus:ring-2 focus:ring-[#69D3C9]"
                    aria-controls="navbar-user" aria-expanded="false">
                    <span class="sr-only">Open main menu</span>
                    <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="#69D3C9"
                        viewBox="0 0 17 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M1 1h15M1 7h15M1 13h15" />
                    </svg>
                </button>
            </div>
            <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-user">
                <ul
                    class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-[#69D3C9] rounded-lg dark:bg-[#001219] bg-[#DFDFDF] md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0">
                    <li>
                        <a href="/"
                            class="block py-2 px-3 dark:text-white text-black rounded hover:bg-[#69D3C9] md:hover:bg-transparent md:hover:text-[#69D3C9] md:p-0">Home</a>
                    </li>
                    <li>
                        <a href="/#/about"
                            class="block py-2 px-3 dark:text-white text-black rounded hover:bg-[#69D3C9] md:hover:bg-transparent md:hover:text-[#69D3C9] md:p-0">About Us</a>
                    </li>
                    <li>
                        <a href="/#/help"
                            class="block py-2 px-3 dark:text-white text-black rounded hover:bg-[#69D3C9] md:hover:bg-transparent md:hover:text-[#69D3C9] md:p-0">Help</a>
                    </li>
                </ul>
            </div>
            
            <div class="items-center flex flex-row w-full md:w-auto md:order-1 pt-1 md:pt-0">
                <img src="src\assets\img\search_24dp_FILL0_wght400_GRAD0_opsz24.svg" alt="Search" class="pe-2">
                <div class="relative z-0">
                    <input type="text" id="search_bar" class="block px-0 md:w-full dark:text-white text-black bg-transparent border-0 border-b-2 dark:border-white border-black appearance-none focus:outline-none focus:ring-0 focus:border-[#69D3C9] peer" placeholder="" />
                    <label for="search_bar" class="absolute md:block hidden dark:text-white text-black duration-300 transform -translate-y-7scale-75 top-0 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-[#69D3C9] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-7 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto">Search Tips...</label>
                </div>
            </div>
        </div>
    </nav>
</header>

<style>
  
</style>
