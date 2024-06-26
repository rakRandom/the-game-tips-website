<script>
    import { fetchImage } from "../api/api_connection";

    import Header from "../components/Header.svelte";
    import HeadlineTemplate from "../components/article_page/HeadlineTemplate.svelte";
    import Footer from "../components/Footer.svelte";
    import { apiLink } from "../stores";

    export let params = {};

    let articleID = params.id;

    let content = [
        {
            game: {
                name: "",
                src: "",
            },
            title: "",
            image: {
                src: "",
                alt: ""
            },
            info: {
                date: "",
                author: {
                    name: "",
                    id: 0,
                    imgSrc: ""
                }
            }
        },
        [
            {
                title: "",
                image: {
                    src: "",
                    alt: ""
                },
                body: [
                    "",
                    ""
                ]
            }
        ]
    ];

    async function getContent() {
        let payload = await fetch($apiLink + "article/" + articleID);
        let request = await payload.json();

        if (!request)
            return;

        content = request;
    }

    getContent();
</script>

<div class="bg-color-0">
    <Header className="sticky top-0" />
    <div class="w-full lg:min-w-[1024px] h-fit lg:min-h-[500px] bg-color-mid text-color-body mx-auto">
        <HeadlineTemplate {...content[0]} />
        <main class="flex flex-col gap-8 flex-1 max-w-[768px] mx-auto mb-10 pb-10">
            <!-- MODELO A SER USADO: -->
            {#each content[1] as element}
            <div class="flex flex-col gap-4 bg-color-mid p-5">
                {#if element.title}
                <h2 class="text-3xl text-color-title break-words hover:translate-x-2 transition-transform cursor-pointer">
                    {element.title}
                </h2>
                {/if}

                {#if element.image}
                <img src={fetchImage(element.image.src)} alt={element.image.alt} class="w-full h-full">
                {/if}

                {#if element.body}
                    {#each element.body as paragraph}
                    <p class="md:text-xl text-lg text-color-body text-justify break-words indent-4">
                        {paragraph}
                    </p>
                    {/each}
                {/if}
            </div>
            {/each}


        </main>
    </div>
    <Footer />
</div>
