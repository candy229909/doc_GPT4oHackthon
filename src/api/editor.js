import request from "@/utils/request";

export function generateData(data) {
  return request({
    url: "/generate",
    method: "post",
    data,
  });
}