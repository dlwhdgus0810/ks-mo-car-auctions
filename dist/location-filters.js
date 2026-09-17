(() => {
  const region=document.querySelector('#region'),yard=document.querySelector('#candidate-yard');
  if(!region||!yard)return;
  const canonical=y=>y==='MO - SPRINGFIELD'?'SPR':y;
  window.yardMatches=(state,location)=>yard.value==='all'||yard.value===`${state}:${canonical(location)}`;
  function refresh(){
    for(const option of yard.options){const valid=option.value==='all'||region.value==='all'||option.value.startsWith(region.value+':');option.hidden=!valid;option.disabled=!valid;}
    if(yard.selectedOptions[0]?.disabled)yard.value='all';
  }
  const params=new URLSearchParams(location.search);
  if(['KS','MO','all'].includes(params.get('region')))region.value=params.get('region');
  refresh();
  if([...yard.options].some(o=>!o.disabled&&o.value===params.get('yard')))yard.value=params.get('yard');
  region.addEventListener('change',refresh);
  yard.addEventListener('change',()=>{
    if(typeof window.filter==='function')window.filter();
    else if(typeof window.render==='function')window.render();
    else if(typeof window.filterTargets==='function')window.filterTargets();
  });
})();
