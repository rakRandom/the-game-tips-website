<script>
    import Router from 'svelte-spa-router';

    import Index from './routes/Index.svelte';
    import Help from './routes/Help.svelte';
    import NotFound from './routes/NotFound.svelte';

    let routes = {
        '/': Index,
        '/help': Help,

        '*': NotFound
    }
</script>

<main>
    <Router {routes} />
</main>
