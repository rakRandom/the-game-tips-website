<script>
    import { fetchImage } from "../api/api_connection";

    import Header from "../components/Header.svelte";
    import Footer from "../components/Footer.svelte";
    import { apiLink } from "../stores";
    import SimpleSection from "../components/SimpleSection.svelte";
    import PopUpArticle from "../components/PopUpArticle.svelte";

    export let params = {};
    let categoryID = params.id;

    let content = {
        gameName: "",
        aboutText: "",
        image: {
        src: "",
        alt: ""
        },
        sections: [
        {
            title: "", 
            seeAllPage: "",
            contents: [
            { 
                gameName: "", 
                title: "", 
                authorPhotoSrc: "", 
                authorName: "", 
                postDate: "", 
                articlePage: ""
            },
            { 
                gameName: "", 
                title: "", 
                authorPhotoSrc: "", 
                authorName: "", 
                postDate: "", 
                articlePage: ""
            },
            { 
                gameName: "", 
                title: "", 
                authorPhotoSrc: "", 
                authorName: "", 
                postDate: "", 
                articlePage: ""
            },
            { 
                gameName: "", 
                title: "", 
                authorPhotoSrc: "", 
                authorName: "", 
                postDate: "", 
                articlePage: ""
            },
            { 
                gameName: "", 
                title: "", 
                authorPhotoSrc: "", 
                authorName: "", 
                postDate: "", 
                articlePage: ""
            },
            ]
        },
        ]
    };

    async function getContent() {
        let payload = await fetch($apiLink + "category/" + categoryID);
        let request = await payload.json();

        if (!request)
            return;

        content = request;
    }

    getContent();
</script>

<div class="bg-color-0">
    <Header className="sticky top-0" />
    <div class="w-full lg:min-w-[1024px] h-fit lg:min-h-[500px] mx-auto bg-color-mid mb-20">
        <div class="max-w-[1280px] mx-auto md:h-3/4 w-full aspect-video">
            <img src={fetchImage(content.image.src)} alt={content.image.alt} class="w-full h-full rounded-b-lg">
        </div>
        <div class="flex flex-col gap-8 w-full h-full md:space-y-5 space-y-3 p-5 max-w-[768px] mx-auto pt-10 pb-20">
            <div class="group w-fit mx-auto">
                <h1 class="md:text-6xl text-4xl text-color-title text-center uppercase cursor-pointer">
                    {content.gameName}
                </h1>
                <hr class="w-0 group-hover:w-full mx-auto border-t-2 border-transparent group-hover:border-[#1E9B8F] dark:group-hover:border-[#69D3C9] transition-all duration-700">
            </div>
            <p class="md:text-xl text-base text-color-body text-justify break-words">
                {content.aboutText}
            </p>
        </div>
        <div class="flex flex-col gap-12 dark:bg-[#001A24] bg-[#EEE] py-20">
            {#each content.sections as sectionData}
            <SimpleSection elementType={PopUpArticle} {...sectionData} />
            {/each}
        </div>
    </div>
    <Footer />
</div>
