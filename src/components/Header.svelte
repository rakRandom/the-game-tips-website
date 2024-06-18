<script>
    export let className = "";
</script>

<div class="z-50 bg-[#001219] w-full md:h-[80px] h-[110px] {className}">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js"></script>
    
    <nav class="md:max-w-[1024px] h-full mx-auto py-2 w-full">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
            <a href="" class="flex items-center md:space-x-3 space-x-1 rtl:space-x-reverse">
                <img src="src\assets\img\help_24dp_FILL0_wght400_GRAD0_opsz24.svg" class="md:h-8 h-7" alt="Logo" />
                <span class="self-center md:text-2xl text-xl font-semibold whitespace-nowrap text-[#69D3C9]">The Game Tips</span>
            </a>
            <div class="flex flex-row items-center md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
                <button>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" fill="#39D3C9" class="md:h-8 pe-3 h-4">
                        <path d="M480-360q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35Zm0 80q-83 0-141.5-58.5T280-480q0-83 58.5-141.5T480-680q83 0 141.5 58.5T680-480q0 83-58.5 141.5T480-280ZM200-440H40v-80h160v80Zm720 0H760v-80h160v80ZM440-760v-160h80v160h-80Zm0 720v-160h80v160h-80ZM256-650l-101-97 57-59 96 100-52 56Zm492 496-97-101 53-55 101 97-57 59Zm-98-550 97-101 59 57-100 96-56-52ZM154-212l101-97 55 53-97 101-59-57Zm326-268Z"/>
                    </svg>
                </button>
                <button>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" fill="#69D3C9" class="md:h-8 pe-3 h-4">
                        <path d="m40-200 210-560h100l210 560h-96l-51-143H187l-51 143H40Zm176-224h168l-82-232h-4l-82 232Zm504 104v-120H600v-80h120v-120h80v120h120v80H800v120h-80Z"/>
                    </svg>
                </button>
                <button type="button"
                    class="flex text-sm bg-gray-800 rounded-full md:me-0 focus:ring-4 focus:ring-[#69D3C9]"
                    id="user-menu-button" aria-expanded="false" data-dropdown-toggle="user-dropdown"
                    data-dropdown-placement="bottom">
                    <span class="sr-only">Open user menu</span>
                    <img class="w-8 h-8 rounded-full" src="src\assets\img\profile picture placeholder.png" alt="user photo">
                </button>
                <!-- Dropdown menu -->
                <div class="z-50 hidden my-4 text-base list-none bg-[#001219] divide-y divide-[#69D3C9] rounded-lg shadow"
                    id="user-dropdown">
                    <div class="px-4 py-3">
                        <span class="block text-sm text-white">User Name</span>
                    </div>
                    <ul class="py-2" aria-labelledby="user-menu-button">
                        <li>
                            <a href="/#/user/:id"
                                class="block px-4 py-2 text-sm text-white hover:text-[#69D3C9]">My Account</a>
                        </li>
                        <li>
                            <a href="#"
                                class="block px-4 py-2 text-sm text-white hover:text-[#69D3C9]">Configurations</a>
                        </li>
                        <li>
                            <a href="#"
                                class="block px-4 py-2 text-sm text-white hover:text-red-600">Sign Out</a>
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
                    class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-[#69D3C9] rounded-lg bg-[#001219] md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-[#001219]">
                    <li>
                        <a href="/"
                            class="block py-2 px-3 text-white rounded hover:bg-[#69D3C9] md:hover:bg-transparent md:hover:text-[#69D3C9] md:p-0">Home</a>
                    </li>
                    <li>
                        <a href="/#/about"
                            class="block py-2 px-3 text-white rounded hover:bg-[#69D3C9] md:hover:bg-transparent md:hover:text-[#69D3C9] md:p-0">About Us</a>
                    </li>
                    <li>
                        <a href="/#/help"
                            class="block py-2 px-3 text-white rounded hover:bg-[#69D3C9] md:hover:bg-transparent md:hover:text-[#69D3C9] md:p-0">Help</a>
                    </li>
                </ul>
            </div>
            
            <div class="items-center flex flex-row w-full md:w-auto md:order-1 pt-1 md:pt-0">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#69D3C9" class="pe-2">
                    <path d="M784-120 532-372q-30 24-69 38t-83 14q-109 0-184.5-75.5T120-580q0-109 75.5-184.5T380-840q109 0 184.5 75.5T640-580q0 44-14 83t-38 69l252 252-56 56ZM380-400q75 0 127.5-52.5T560-580q0-75-52.5-127.5T380-760q-75 0-127.5 52.5T200-580q0 75 52.5 127.5T380-400Z"/>
                </svg>
                <div class="relative z-0">
                    <input type="text" id="search_bar" class="block px-0 md:w-full text-white bg-transparent border-0 border-b-2 border-white appearance-none focus:outline-none focus:ring-0 focus:border-[#69D3C9] peer" placeholder="" />
                    <label for="search_bar" class="absolute md:block hidden text-white duration-300 transform -translate-y-7scale-75 top-0 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-[#69D3C9] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-7 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto">Search Tips...</label>
                </div>
            </div>
        </div>
    </nav>
</div>

<style>
  
</style>
