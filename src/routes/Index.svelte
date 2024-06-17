<script>
    // Todo: Security test (text overflow, layout overflow, right position, responsivity etc)
    // Todo: Responsivity (follow mobile-first principles)
    // Todo: Add Black and White themes
    // Todo: Add class "uppercase" to the titles that need all the letters to be uppercase

    import { title } from '.././stores.js';
    import Header from '.././components/Header.svelte'
    import MainArticle from '.././components/landing_page/MainArticle.svelte';
    import SimpleSection from '.././components/SimpleSection.svelte';
    import BulletTipItem from '.././components/landing_page/BulletTipItem.svelte';
    import PopUpArticle from '.././components/PopUpArticle.svelte';
    import MidArticle from '.././components/landing_page/MidArticle.svelte';
    import CategoryBar from '.././components/landing_page/CategoryBar.svelte';

    import Footer from '.././components/Footer.svelte';

    function isInViewport(element) {
        if (!element)
            return;

        var rect = element.getBoundingClientRect();
        var html = document.documentElement;
        
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || html.clientHeight) &&
            rect.right <= (window.innerWidth || html.clientWidth)
        );
    }

    window.addEventListener("scroll", (e) => {
        let element = document.getElementById("goc-underline");
        if (isInViewport(element)) {
            element.classList.remove("w-0");
            element.classList.add("w-[75%]");
        }
    });
</script>

<svelte:head>
    <title>{$title()}</title> 
</svelte:head>

<div class="w-full min-h-screen bg-[#001219]">
    <Header className="sticky top-0" />
    <MainArticle />

    <div class="mt-12">
        <SimpleSection 
            className="mt-8"
            title="Bullet Tips" 
            elementsQt="9"
            innerElements={[
                BulletTipItem, BulletTipItem, BulletTipItem, BulletTipItem, BulletTipItem, 
                BulletTipItem, BulletTipItem, BulletTipItem, BulletTipItem
            ]} 
            elementsValues={[
                {name: "YO BRO COME OVER HERE"},
                {name: "CHECK OUT MY NEW SHOES"},
                {name: "THATS A BRAND NEW"},
                {name: "ONE, TWO, BUCKLE"},
                {name: "ON MY SHOOOOOES"},
                {name: "THREE, FOUR, BUCKLE"},
                {name: "SOME MOOOOORE"},
                {name: "FIVE, SIX, NIKE KICKS"},
                {name: "HAHAHAHA THATS SO FIRE"}
            ]}
        />

        <hr class="max-w-[1024px] mx-auto mt-14 mb-20">

        <div class="flex flex-col gap-20 mt-4">
            <SimpleSection 
                title="Newest Posts" 
                elementsQt="4"
                innerElements={[
                    PopUpArticle, PopUpArticle, PopUpArticle, PopUpArticle
                ]} 
            />
            <SimpleSection 
                title="Newest Posts" 
                elementsQt="3"
                innerElements={[
                    PopUpArticle, PopUpArticle, PopUpArticle
                ]} 
            />

            <MidArticle />
        </div>
    </div>

    <div class="mt-40">
        <div class="w-fit mx-auto">
            <h2 class="text-[#2EC4B6] text-[38px] font-normal">TIPS FOR YOUR GAME OF CHOICE</h2>
            <hr id="goc-underline" 
                class="w-0 mx-auto border-[1px] border-[#2EC4B6] 
                    transition-all delay-0 duration-1000">
        </div>

        <div class="flex flex-col gap-[100px] mt-[100px]">
            <CategoryBar 
                gameTitle="MULTIVERSUS"
                description="Descrição bem longa sobre o jogo multiversus, uau, como esse texto é longo. Meu deus, não consigo acreditar, tem um segundo parágrafo, isso só pode ser coisa de textos enormes, tipo aqueles feitos pelo meu mano Machado de Assis, aquele que criou uns livros lá, tipo “O Guarani”, eu acho."
                categoryPage=""
            />
            <CategoryBar 
                gameTitle="GOD OF WAR"
                description=""
                categoryPage=""
            />
            <CategoryBar 
                gameTitle="THE LAST OF US"
                description=""
                categoryPage=""
            />
        </div>
    </div>

    <Footer className="mt-40"/>
</div>


<style>
  
</style>

