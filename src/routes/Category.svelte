<script>
  import Header from "../components/Header.svelte";
  import CategoryTemplate from "./templates/CategoryTemplate.svelte";
  import Footer from "../components/Footer.svelte";

  let id = 0;

  const values = [
    {
      gamename: "God of War",
      aboutText:
        "God of War is an action-adventure video game developed by Santa Monica Studio and published by Sony Interactive Entertainment. It was released on April 20, 2018 for PlayStation 4 and on January 14, 2022 for Microsoft Windows.",
    },
  ];
</script>

<div>
  <Header className="sticky top-0" />
  <CategoryTemplate {...values[0]} />
  <Footer />
</div>
