<script>
    import Header from "../components/Header.svelte";
    import HeadlineTemplate from "../components/article_page/HeadlineTemplate.svelte";
    import Footer from "../components/Footer.svelte";
    import { apiLink } from "../stores";

    export let params = {};

    let articleID = params.id;

    let content = [
        {

        },
        [
            {
                title: "",
                image: {
                    src: "",
                    alt: ""
                },
                body: [
                    "Parágrafo 1",
                    "Parágrafo 2"
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

<div class="w-full min-h-screen bg-[#F6F6F6] dark:bg-[#000B10] text-color-body">
    <Header className="sticky top-0" />
    <HeadlineTemplate {...content[0]} />
    <main class="flex flex-col gap-16 flex-1 max-w-[1024px] w-full mx-auto py-24">
        <!-- MODELO A SER USADO: -->
        {#each content[1] as element}
        <div class="">
            {#if element.title}
            <h2 class="">
                {element.title}
            </h2>
            {/if}

            {#if element.image}
            <img src={element.image.src} alt={element.image.alt} class="">
            {/if}

            {#if element.body}
                {#each element.body as paragraph}
                <p class="">
                    {paragraph}
                </p>
                {/each}
            {/if}
        </div>
        {/each}

        <!-- DELETAR CONTEÚDO ABAIXO -->
        <div class="justify-center">
        <p class="text-2xl text-justify">
            If you want a melee build in Elden Ring, it's a good idea to invest
            points in strength or dexterity. This helps meet the minimum
            requirements for many weapons and also increases the damage done by
            them.
        </p>
        </div>
        <div>
        <p class="text-2xl text-justify">
            Halberds, like the Lucerne, generally rely on your strength or
            dexterity. They offer a long range and are enough levels to keep your
            character agile. While you may switch weapons a few times throughout the
            game, it's crucial to find a great weapon early in the game that will
            help you reach the more advanced areas.
        </p>
        </div>
        <div>
        <h2 class="text-4xl text-justify font-title-semibold my-10">
            Where to Find Lucerne
        </h2>
        <img src="mapEldenRing.svg" alt="Map Elden Ring" />
        <p class="text-2xl text-justify mt-8">
            You can find Lucerne just after passing Stormveil Castle. Cross Liurnia
            dos Lagos and head east, where you will find the free point on the
            Estrada Norte da Liurnia. Follow the broken road north until you reach a
            battlefield between soldiers and ghosts. More ghosts will appear shortly
            after you arrive, and if you continue a little further down the road, a
            giant ghost will appear to the right of the path.
        </p>
        </div>
        <div>
        <h2 class="text-4xl text-justify font-title-semibold my-10">
            Lucerne Map Location
        </h2>
        <p class="text-2xl text-justify mt-8">
            The Lucerne is located among some of the destroyed wagons to the right
            of the path. With the large number of enemies, it is easy to initially
            move unseen and destroy carts outside of combat range. There are other
            valuable items scattered across the battlefield, further encouraging you
            to defeat all enemies present. This is also an excellent place to
            collect runes early in the game, as many enemies kill each other,
            rewarding you with runes. After destroying the wagons, you will find
            Lucerne among the wreckage.
        </p>
        </div>
        <div>
        <h2 class="text-4xl text-justify font-title-semibold my-10">
            How to use Lucerne
        </h2>
        <img
            src="setImageEldenRing.svg"
            alt="Set equipament Elden Ring"
        />
        <p class="text-2xl text-justify mt-8">
            The Lucerne requires 15 Strength and 12 Dexterity to use. Despite
            requiring more strength, this weapon scales more with dexterity,
            reaching a 'B' at its highest levels. This level of scaling is semi-rare
            in the early sections of the game, making Lucerne an excellent option
            for dexterity-based builds who also want to maintain a safe distance
            during combat. Halberd-style weapons are great for dexterity builds, as
            their light weight and reach help you fight from a distance and quickly
            reposition if necessary.
        </p>
        </div>
        <div>
        <p class="text-2xl text-justify mt-8">
            This weapon deals piercing damage and comes with the “Charge Forth”
            ability. This ability costs 16 FP to cast and can quickly close the
            distance between you and more distant enemies. This ability is great for
            starting fights and benefiting even more from a dexterity build that can
            retreat after the initial attack. The weapon can also be infused with
            other Ashes of War to increase its characteristics and better suit your
            build.
        </p>
        <p class="text-color-title flex justify-center mt-10">
            _______________________________________________________________________________________________________________________________________________________
        </p>
        </div>
    </main>
    <Footer />
</div>
