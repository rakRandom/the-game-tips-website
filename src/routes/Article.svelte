<script>
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

<!-- estilização temporária até adição de um artigo para visualizar como ficou e melhorar o que for necessário-->
<div class="w-full min-h-screen bg-color-0 text-color-body">
    <Header className="sticky top-0" />
    <HeadlineTemplate {...content[0]} />
    <main class="flex flex-col gap-16 flex-1 max-w-[1024px] w-full mx-auto py-24">
        <!-- MODELO A SER USADO: -->
        {#each content[1] as element}
        <div class="bg-color-mid p-5">
            {#if element.title}
            <h2 class="md:text-2xl text-lg text-color-title break-words">
                {element.title}
            </h2>
            {/if}

            {#if element.image}
            <img src={element.image.src} alt={element.image.alt} class="">
            {/if}

            {#if element.body}
                {#each element.body as paragraph}
                <p class="md:text-lg text-base text-color-body text-justify break-words">
                    {paragraph}
                </p>
                {/each}
            {/if}
        </div>
        {/each}

    </main>
    <Footer />
</div>
