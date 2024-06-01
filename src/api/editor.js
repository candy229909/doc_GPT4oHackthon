import request from "@/utils/request";

export function generateData(data) {
  return request({
    url: "/api/generate",
    method: "post",
    data,
  });
}