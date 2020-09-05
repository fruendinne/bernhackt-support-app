import axios from 'axios'

const API_HOST = 'http://localhost:8000'
const API_ROOT = '/api/v1/support'

export class Flow {
  static STATE_OPEN = 0
  static STATE_SUCCESSFUL = 1
  static STATE_UNSUCCESSFUL = 2

  constructor(obj) {
    obj && Object.assign(this, obj);
  }
}

export async function startFlow (userQuery) {
  try {
    return new Flow((await axios.get(API_HOST + API_ROOT + '/start_flow?user_query=' + userQuery)).data)
  } catch (error) {
    console.error(error);
  }
}

export async function getNextTLB (flow) {
  try {
    return (await axios.get(API_HOST + API_ROOT + '/next_tlb/' + flow.pk)).data
  } catch (error) {
    console.error(error);
  }
}

export async function setSuccess (flow) {
  try {
    return (await axios.get(API_HOST + API_ROOT + '/set_success/' + flow.pk)).data
  } catch (error) {
    console.error(error);
  }
}
