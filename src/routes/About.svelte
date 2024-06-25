<script>
    import { getContent } from "../api/api_connection";

    import Header from ".././components/Header.svelte";
    import MainAbout from "../components/about_page/MainAbout.svelte";
    import AboutDevTemplate from "../components/about_page/AboutDevTemplate.svelte";
    import Footer from ".././components/Footer.svelte";

    let valores = [
        { 
            name: "", 
            image: "", 
            linkedin: "", 
            github: "", 
            whatsapp: "",  
            email: "", 
            description: "" 
        }
    ];

    async function load() { 
        valores = await getContent("get-author");
    };
    load();
</script>

<div class="w-full min-h-screen bg-color-0">
    <Header className="sticky top-0" />
    <MainAbout />
    <hr class="lg:hidden max-w-[1024px] mx-[16px] md:mx-[32px] mt-16 border-t-2">
    <div class="flex items-center justify-center m-5 mt-16">
        <h1
        class="text-[#69D3C9] text-[36px] font-title-semibold block text-center"
        >
            Our Team
        </h1>
    </div>
    <div class="max-w-[768px] mx-auto md:px-[32px] xl:px-0">
        {#each valores as valor}
            <AboutDevTemplate {...valor} />
        {/each}
    </div>
    <hr class="lg:hidden max-w-[1024px] mx-[16px] md:mx-[32px] mt-16 border-t-2">
    <div class="flex items-center justify-center mb-10 max-w-[1024px] mx-auto">
        <h2 class="text-color-body text-[36px] font-title-bold block text-center my-36 px-[16px] md:px-[100px]">
            Success is not definitive, failure is not fatal: It is the courage to
            continue that counts.
        </h2>
    </div>
    <Footer />
</div>
