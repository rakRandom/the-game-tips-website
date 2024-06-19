<script>
  import Header from "../components/Header.svelte";
  import CategoryTemplate from "./templates/CategoryTemplate.svelte";
  import Footer from "../components/Footer.svelte";

  let id = 0;

  const values = [
    {
      gamename: "Multiversus",
      aboutText:
        "Enter the fray of the MultiVerse, where each match is a big mess of iconic characters facing off in hilariously different ways. Combine Marvin the Martian and Arya Stark, or Velma with Batman — Get ready for a rollercoaster of fun and discover a universe of endless possibilities!",
    },
  ];
</script>

<div>
  <Header className="sticky top-0" />
  <CategoryTemplate {...values[id]} />
  <Footer />
</div>
