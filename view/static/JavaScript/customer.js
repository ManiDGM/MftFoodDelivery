function edit(id){

}

async function remove(id){
    await fetch("/customer?id="+id, {
        method:"DELETE"
    });

    document.location.replace("/customer");
}