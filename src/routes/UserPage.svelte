<script>
    export let params = {};
    let isUser = params.id.split("i")[0];
    let userID = params.id.split("i")[1];

</script>

<div>
    <p>{isUser}</p>
    <p>{userID}</p>
</div>
